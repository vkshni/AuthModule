# Storage

import sqlite3
from pathlib import Path
import sys

# Adding project root to the python path
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from models.user import User


# User DB
class UserDB:

    def __init__(self):
        self.db_path = PROJECT_ROOT / "data" / "users.db"
        self.db_path.parent.mkdir(exist_ok=True)

    # Get conneciton
    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(str(self.db_path))

    # Create table
    def create_table(self) -> bool:

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                # Execute
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS user(
                            id TEXT PRIMARY KEY,
                            email TEXT UNIQUE,
                            password_hash TEXT NOT NULL,
                            created_at TEXT NOT NULL,
                            role TEXT)"""
                )
            return True
        except Exception as e:
            return False

    # Add user
    def add_user(self, user) -> bool:

        user_dict = user.to_dict()
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                # Execute
                cursor.execute(
                    "INSERT INTO user(id, email, password_hash, created_at, role) VALUES (?,?,?,?,?)",
                    (
                        user_dict.get("id"),
                        user_dict.get("email"),
                        user_dict.get("password_hash"),
                        user_dict.get("created_at"),
                        user_dict.get("role"),
                    ),
                )
            return True
        except Exception as e:
            return False

    # Get user by email
    def get_user_by_email(self, email: str) -> User | bool | None:

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                # Execute
                cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
                result = cursor.fetchall()
        except:
            return False

        if not result:
            return

        USER_FIELDS = ["id", "email", "password_hash", "created_at", "role"]
        row = result[0]
        user_dict = dict(zip(USER_FIELDS, row))

        # Deserialization
        user = User.from_dict(user_dict)

        return user

    # Get user by ID
    def get_user_by_id(self, user_id: str) -> User | bool | None:

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                # Execute
                cursor.execute("SELECT * FROM user WHERE id = ?", (user_id,))
                result = cursor.fetchall()
        except:
            return False

        if not result:
            return

        USER_FIELDS = ["id", "email", "password_hash", "created_at", "role"]
        row = result[0]
        user_dict = dict(zip(USER_FIELDS, row))

        # Deserialization
        user = User.from_dict(user_dict)

        return user

    # Email exists
    def email_exists(self, email: str) -> bool:

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                # Execute
                cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
                result = cursor.fetchone()

            return result is not None
        except:
            return False


if __name__ == "__main__":

    userdb = UserDB()
    # # userdb.create_table()
    print(userdb.email_exists("vks@gmail.com"))
    # with sqlite3.connect("users.db") as conn:
    #     cursor = conn.cursor()

    #     cursor.execute("DELETE FROM users where email='vks@gmail.com'")
