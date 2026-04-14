# Models

# Libraries
from uuid import uuid4
from datetime import datetime

# DATETIME FORMAT
DATETIME_FORMAT = "%d-%m-%YT%H:%M:%S"


# User entity
class User:

    def __init__(
        self,
        email: str,
        password_hash: str,
        role: str = "USER",
        created_at: str = None,
        id: str = None,
    ):
        self.id = str(id) if id else str(uuid4())
        self.email = email
        self.password_hash = password_hash
        self.created_at = (
            datetime.strptime(created_at, DATETIME_FORMAT)
            if created_at
            else datetime.now()
        )
        self.role = role

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at.strftime(DATETIME_FORMAT),
            "role": self.role,
        }

    @classmethod
    def from_dict(cls, user_dict: dict) -> "User":
        return cls(
            email=user_dict.get("email"),
            password_hash=user_dict.get("password_hash"),
            role=user_dict.get("role"),
            created_at=user_dict.get("created_at"),
            id=user_dict.get("id"),
        )

    def __str__(self):
        return f"User(email={self.email}, password_hash={self.password_hash}, role={self.role}, created_at={self.created_at}, id={self.id})"


if __name__ == "__main__":
    u1 = User("vks@gmail.com", password_hash="xyz")
    print(u1)
    print(u1.to_dict())
    user_dict = u1.to_dict()
    print(User.from_dict(user_dict))
