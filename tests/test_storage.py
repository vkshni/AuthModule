import sys
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from storage.user_db import UserDB
from models.user import User

# Test database
TEST_DB = PROJECT_ROOT / "data" / "test_users.db"


def setup():
    """Create test database"""
    try:
        if TEST_DB.exists():
            os.remove(TEST_DB)
    except:
        pass
    


def teardown():
    """Clean up test database"""
    try:
        if TEST_DB.exists():
            os.remove(TEST_DB)
    except:
        pass


def test_create_table():
    """Test table creation"""
    setup()
    db = UserDB()
    db.db_path = TEST_DB
    result = db.create_table()
    assert result == True
    print("✓ Table creation works")


def test_add_user():
    """Test adding user"""
    db = UserDB()
    db.db_path = TEST_DB
    db.create_table()
    
    user = User("test@test.com", "hash123")
    result = db.add_user(user)
    assert result == True
    print("✓ Add user works")


def test_get_user_by_email():
    """Test getting user by email"""
    db = UserDB()
    db.db_path = TEST_DB
    
    user = db.get_user_by_email("test@test.com")
    assert user is not None
    assert user.email == "test@test.com"
    print("✓ Get user by email works")


def test_get_user_not_found():
    """Test getting non-existent user"""
    db = UserDB()
    db.db_path = TEST_DB
    
    user = db.get_user_by_email("notfound@test.com")
    assert user is None
    print("✓ Get non-existent user returns None")


def test_email_exists():
    """Test email existence check"""
    db = UserDB()
    db.db_path = TEST_DB
    
    exists = db.email_exists("test@test.com")
    assert exists == True
    
    not_exists = db.email_exists("fake@test.com")
    assert not_exists == False
    print("✓ Email exists check works")


if __name__ == "__main__":
    test_create_table()
    test_add_user()
    test_get_user_by_email()
    test_get_user_not_found()
    test_email_exists()
    teardown()
    print("\n✅ All storage tests passed!")