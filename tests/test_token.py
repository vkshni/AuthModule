import sys
from pathlib import Path
import time

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.tokens import generate_token, verify_token
from models.user import User


def test_generate_token():
    """Test token generation"""
    user = User("test@test.com", "hash123")
    token = generate_token(user)
    assert token is not False
    assert len(token) > 50
    print("✓ Token generation works")


def test_verify_token_valid():
    """Test valid token verification"""
    user = User("test@test.com", "hash123")
    token = generate_token(user)
    success, payload = verify_token(token)
    
    assert success == True
    assert payload["email"] == "test@test.com"
    assert "sub" in payload
    print("✓ Valid token verification works")


def test_verify_token_invalid():
    """Test invalid token rejection"""
    success, msg = verify_token("invalid.token.here")
    assert success == False
    assert "Invalid" in msg or "token" in msg.lower()
    print("✓ Invalid token rejected")


def test_token_payload_content():
    """Test token contains correct payload"""
    user = User("payload@test.com", "hash123", role="ADMIN")
    token = generate_token(user)
    success, payload = verify_token(token)
    
    assert payload["email"] == "payload@test.com"
    assert payload["role"] == "ADMIN"
    assert payload["sub"] == user.id
    print("✓ Token payload correct")


if __name__ == "__main__":
    test_generate_token()
    test_verify_token_valid()
    test_verify_token_invalid()
    test_token_payload_content()
    print("\n✅ All token tests passed!")