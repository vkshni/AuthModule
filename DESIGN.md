# AuthModule - DESIGN DOCUMENT

## Overview
### About
Autharization module that can be integrated in any real world system

### Core features
- User Registration/login (Multi-user)
- Password hashing
- Token payload structure (JWT)
- Basic middleware
- Framework agnostic

## Architecture
```bash
auth-module/
├── core/
│   ├── auth.py          # Main auth logic
│   ├── tokens.py        # JWT generation/validation
│   └── passwords.py     # Hashing/verification
├── models/
│   └── user.py          # User entity
├── storage/
│   └── user_db.py       # User persistence
├── middleware/
│   └── auth_middleware.py  # Protect routes
├── validators/
│   └── validators.py    # Input validation
├── config/
│   └── settings.py      # Environment config
└── tests/
```

## Data models
- User schema (id, name, password_hash, created_at, role)
- Token Payload Structure

## Security Decisions
- Hashing algorithm: bcrypt
- Token type: JWT
- Token expiry: 1 hour
- Password requirements: min 8 chars, 1 letter, 1 number
- Storage: SQLite 

## Interface layer
Command Line Interface (CLI)

## Configuration
- Environment variables: SECRET_KEY, TOKEN_EXPIRY
- Default settings
- Security best practices

##  Error Handling
- Invalid credentials
- Token expired
- User already exists
- Validation errors

## Files and their contents

### Models/
- `user.py`
    ```python
    class User:
        def __init__():
        def to_dict() -> dict:
        def from_dict(user_dict) -> 'User':
        def __str__() -> str:
    ```
### Core/
- `passwords.py`
Uses bcrypt hashing
    ```python
    def hash_password(plain_password) -> str | bool:
    def verify_password(plain_password, hashed) -> bool:
    ```
### Storage/
- `user_db.py`
    ```python
    class UserDB:
        def __init__():
        def _get_connection() -> Connection:
        def create_table() -> bool:
        def add_user(user: User) -> bool:
        def get_user_by_email(email) -> User | bool | None:
        def get_user_by_id(id) -> User | bool | None:
        def email_exists(email) -> bool:

    
