# Storage

import sqlite3

# from models.user import User


# User DB
class UserDB:

    def __init__(self):
        pass

    # Create table
    def create_table(self):
        with sqlite3.connect("users.db") as conn:
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

    # Add user
    def add_user(self, user):

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()

            # Execute
            cursor.execute(
                "INSERT INTO user(id, email, password_hash, created_at, role) VALUES (?,?,?,?,?)",
                (user.id, user.email, user.password_hash, user.created_at, user.role),
            )
        return True

    # Email exists
    def email_exists(self, email: str) -> bool:

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()

            # Execute
            cursor.execute(f"SELECT * FROM user WHERE email = {email}")
            result = cursor.fetchall()

        if result:
            return True
        else:
            False


if __name__ == "__main__":

    userdb = UserDB()
    # userdb.create_table()
    userdb.email_exists("vks@gmail.com")
