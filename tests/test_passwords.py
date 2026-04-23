import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.passwords import hash_password, verify_password


def test_hash_password():
    """Test password hashing"""
    hashed = hash_password("test123")
    assert hashed != "test123", "Password should be hashed"
    assert len(hashed) > 50, "Hash should be long"
    print("✓ Hash password works")


def test_verify_password_correct():
    """Test correct password verification"""
    hashed = hash_password("mypassword")
    result = verify_password("mypassword", hashed)
    assert result == True, "Should verify correct password"
    print("✓ Verify correct password works")


def test_verify_password_wrong():
    """Test wrong password verification"""
    hashed = hash_password("mypassword")
    result = verify_password("wrongpass", hashed)
    assert result == False, "Should reject wrong password"
    print("✓ Verify wrong password works")


def test_different_hashes():
    """Test same password produces different hashes"""
    hash1 = hash_password("test123")
    hash2 = hash_password("test123")
    assert hash1 != hash2, "Same password should produce different hashes (salt)"
    print("✓ Different hashes for same password")


if __name__ == "__main__":
    test_hash_password()
    test_verify_password_correct()
    test_verify_password_wrong()
    test_different_hashes()
    print("\n✅ All password tests passed!")