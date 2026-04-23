import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models.user import User


def test_user_creation():
    """Test user object creation"""
    user = User("test@test.com", "hashed_pass", role="USER")
    assert user.email == "test@test.com"
    assert user.password_hash == "hashed_pass"
    assert user.role == "USER"
    assert user.id is not None
    print("✓ User creation works")


def test_user_to_dict():
    """Test user serialization"""
    user = User("test@test.com", "hash123")
    data = user.to_dict()
    
    assert data["email"] == "test@test.com"
    assert data["password_hash"] == "hash123"
    assert "id" in data
    assert "created_at" in data
    print("✓ User to_dict works")


def test_user_from_dict():
    """Test user deserialization"""
    data = {
        "id": "test-123",
        "email": "test@test.com",
        "password_hash": "hash123",
        "role": "ADMIN",
        "created_at": "01-01-2024T12:00:00"
    }
    user = User.from_dict(data)
    
    assert user.id == "test-123"
    assert user.email == "test@test.com"
    assert user.role == "ADMIN"
    print("✓ User from_dict works")


def test_user_default_role():
    """Test default role is USER"""
    user = User("test@test.com", "hash123")
    assert user.role == "USER"
    print("✓ Default role works")


if __name__ == "__main__":
    test_user_creation()
    test_user_to_dict()
    test_user_from_dict()
    test_user_default_role()
    print("\n✅ All user tests passed!")