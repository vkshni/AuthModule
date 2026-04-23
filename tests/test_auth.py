import sys
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.auth import AuthService
from storage.user_db import UserDB

TEST_DB = PROJECT_ROOT / "data" / "test_auth.db"


def setup():
    """Setup test database"""
    if TEST_DB.exists():
        try:
            os.remove(TEST_DB)
        except PermissionError:
            pass  # File in use, will overwrite
    
    db = UserDB()
    db.db_path = TEST_DB
    return AuthService(db)


def teardown():
    """Clean up test database"""
    import time
    time.sleep(0.1)  # Let connections close
    
    try:
        if TEST_DB.exists():
            os.remove(TEST_DB)
    except PermissionError:
        pass  # File still in use, ignore


def test_register_success():
    """Test successful registration"""
    auth = setup()
    success, data = auth.register("test@test.com", "password123")
    assert success == True
    assert len(data) > 10  # UUID length
    print("✓ Register success works")


def test_register_duplicate():
    """Test duplicate email registration"""
    auth = setup()
    auth.register("dup@test.com", "password123")
    success, msg = auth.register("dup@test.com", "password456")
    assert success == False
    assert "already exists" in msg
    print("✓ Register duplicate blocked")


def test_register_weak_password():
    """Test weak password rejection"""
    auth = setup()
    success, msg = auth.register("weak@test.com", "weak")
    assert success == False
    assert "password" in msg.lower()
    print("✓ Weak password rejected")


def test_register_invalid_email():
    """Test invalid email rejection"""
    auth = setup()
    success, msg = auth.register("bademail", "password123")
    assert success == False
    assert "email" in msg.lower()
    print("✓ Invalid email rejected")


def test_login_success():
    """Test successful login"""
    auth = setup()
    auth.register("login@test.com", "password123")
    success, token = auth.login("login@test.com", "password123")
    assert success == True
    assert len(token) > 50  # JWT token length
    print("✓ Login success works")


def test_login_wrong_password():
    """Test login with wrong password"""
    auth = setup()
    auth.register("wrong@test.com", "password123")
    success, msg = auth.login("wrong@test.com", "wrongpass")
    assert success == False
    assert "Invalid credentials" in msg
    print("✓ Wrong password rejected")


def test_login_nonexistent_user():
    """Test login with non-existent user"""
    auth = setup()
    success, msg = auth.login("fake@test.com", "password123")
    assert success == False
    assert "Invalid credentials" in msg
    print("✓ Non-existent user rejected")


if __name__ == "__main__":
    test_register_success()
    test_register_duplicate()
    test_register_weak_password()
    test_register_invalid_email()
    test_login_success()
    test_login_wrong_password()
    test_login_nonexistent_user()
    teardown()
    print("\n✅ All auth tests passed!")