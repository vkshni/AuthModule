# AuthModule

A lightweight authentication module for Python applications. This project provides user registration, password hashing, JWT token generation/validation, storage persistence, and route protection middleware.

## Overview

AuthModule is designed to be framework-agnostic and easy to integrate into CLI or web applications. It supports:
- User registration with email validation
- Secure password hashing using `bcrypt`
- Login and token issuance using JSON Web Tokens (`PyJWT`)
- SQLite-backed user persistence
- Simple middleware for protecting routes

## Features

- `AuthService` for user registration, login, and credential verification
- `UserDB` for SQLite persistence in `data/users.db`
- `bcrypt` password hashing and verification
- JWT tokens with a 1-hour expiry
- Email/password validation
- Middleware helper to validate tokens and extract user context

## Project Structure

- `core/`
  - `auth.py` - authentication service and registration/login workflows
  - `passwords.py` - password hashing and verification helpers
  - `tokens.py` - JWT generation and verification
- `models/`
  - `user.py` - user entity and serialization helpers
- `storage/`
  - `user_db.py` - SQLite persistence layer for users
- `middleware/`
  - `auth_middleware.py` - token-based route protection helper
- `validators/`
  - `validators.py` - email and password validation logic
- `data/`
  - `users.db` - SQLite database file created at runtime
- `tests/` - unit tests for the auth module

## Installation

1. Activate the Python virtual environment:

```powershell
& .\authenv\Scripts\Activate.ps1
```

2. Install dependencies if needed:

```powershell
pip install bcrypt PyJWT
```

## Configuration

The module reads the JWT secret from the environment variable `JWT_SECRET_KEY`. If not set, it defaults to `dev-secret-only`.

Example:

```powershell
$env:JWT_SECRET_KEY = "your-secret-key"
```

## Usage

Example usage with the auth service:

```python
from core.auth import AuthService
from storage.user_db import UserDB

user_db = UserDB()
auth = AuthService(user_db)

success, result = auth.register("user@example.com", "Password123")
if success:
    print("Registered user id:", result)
else:
    print("Register failed:", result)

success, token = auth.login("user@example.com", "Password123")
if success:
    print("JWT token:", token)
else:
    print("Login failed:", token)
```

Verify a JWT token:

```python
from core.tokens import verify_token

is_valid, payload = verify_token(token)
if is_valid:
    print("Token payload:", payload)
else:
    print("Token error:", payload)
```

Protect a route with middleware:

```python
from middleware.auth_middleware import protect_route

is_valid, context = protect_route(token)
if is_valid:
    print("Authorized user:", context)
else:
    print("Authorization failed:", context)
```

## Testing

Run the unit tests using `pytest` from the repository root:

```powershell
pytest
```

## Design

For architecture, data models, and design decisions, see `DESIGN.md`.

## License

This repository does not currently include a license file. Add one if you plan to distribute the code.
