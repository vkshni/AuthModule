import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from middleware.auth_middleware import protect_route
from core.tokens import generate_token
from models.user import User


def test_protect_route_valid_token():
    """Test middleware with valid token"""
    user = User("test@test.com", "hash123", role="USER")
    token = generate_token(user)
    
    success, data = protect_route(token)
    assert success == True
    assert data["user_id"] == user.id
    assert data["role"] == "USER"
    print("✓ Protect route with valid token works")


def test_protect_route_invalid_token():
    """Test middleware with invalid token"""
    success, msg = protect_route("invalid.token.here")
    assert success == False
    print("✓ Protect route blocks invalid token")


def test_protect_route_missing_token():
    """Test middleware with no token"""
    success, msg = protect_route("")
    assert success == False
    print("✓ Protect route blocks empty token")


if __name__ == "__main__":
    test_protect_route_valid_token()
    test_protect_route_invalid_token()
    test_protect_route_missing_token()
    print("\n✅ All middleware tests passed!")