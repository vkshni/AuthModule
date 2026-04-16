# Auth logic

# Libraries
from pathlib import Path
import sys

# Adding Project Root to the Python path
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Project modules
from passwords import hash_password, verify_password
from storage.user_db import UserDB
from models.user import User


# UserDB
# userdb = UserDB()
# userdb.create_table()


class AuthService:

    def __init__(self, user_db: UserDB):
        self.user_db = user_db

    # Register User (first-time)
    def register(self, email: str, password: str, role: str = "USER"):

        existing = self.user_db.get_user_by_email(email)
        if existing:
            return (False, f"Email already exists")

        password_hash = hash_password(password)
        user = User(email, password_hash, role=role.upper())

        added = self.user_db.add_user(user)
        return (True, user.id)

    # Login
    def login(self, email: str, password: str):

        existing = self.user_db.get_user_by_email(email)
        if not existing:
            return (False, f"No user found with email '{email}'")

        is_authenticate = verify_password(password, existing.password_hash)
        if is_authenticate:
            # JWT Token logic
            return (True, "token")

        return (False, "Incorrect password")

    # Verify credentials
    def verify_credentials(self, email: str, password: str):

        existing = self.user_db.get_user_by_email(email)
        if not existing:
            return (False, f"No user found with email '{email}'")

        is_authenticate = verify_password(password, existing.password_hash)
        if is_authenticate:
            return (True, "")

        return (False, "Incorrect password")


if __name__ == "__main__":

    # Test 1: Register new user
    auth = AuthService(UserDB())
    success, msg = auth.register("test@example.com", "password123")
    print(success, msg)  # Should be (True, user_id)

    # Test 2: Register duplicate email
    success, msg = auth.register("test@example.com", "pass456")
    print(success, msg)  # Should be (False, "Email already exists")

    # Test 3: Register weak password
    success, msg = auth.register("new@example.com", "weak")
    print(success, msg)  # Should be (False, "Password too weak")

    # Test 4: Login success
    success, data = auth.login("test@example.com", "password123")
    print(success, data)  # Should be (True, user_id) for now

    # Test 5: Login wrong password
    success, data = auth.login("test@example.com", "wrongpass")
    print(success, data)  # Should be (False, "Invalid credentials")

    # Test 6: Login non-existent user
    success, data = auth.login("fake@example.com", "pass123")
    print(success, data)  # Should be (False, "Invalid credentials")
