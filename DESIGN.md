# AuthModule - DESIGN DOCUMENT

## Overview

AuthModule is a lightweight, framework-agnostic authentication library for Python applications. It provides user registration, secure password handling, JWT token issuance and verification, SQLite-backed persistence, and simple middleware for protecting routes.

## Core Features

- User registration with email validation
- Password hashing and verification using `bcrypt`
- JWT token creation and validation via `PyJWT`
- SQLite persistence for users stored in `data/users.db`
- Basic middleware for token-based route protection
- Input validation for email and password strength

## Architecture

```
auth-module/
├── core/
│   ├── auth.py          # Main auth logic and workflows
│   ├── tokens.py        # JWT generation and verification
│   └── passwords.py     # Password hashing and verification
├── models/
│   └── user.py          # User entity and serialization
├── storage/
│   └── user_db.py       # SQLite persistence for users
├── middleware/
│   └── auth_middleware.py  # Token validation helper for protected routes
├── validators/
│   └── validators.py    # Email and password validation
├── data/
│   └── users.db         # Database file created at runtime
├── tests/
│   └── ...              # Unit tests
├── README.md
└── DESIGN.md
```

## Data Models

### User

The `User` entity consists of:
- `id`: UUID string primary key
- `email`: email address
- `password_hash`: bcrypt hashed password
- `created_at`: timestamp string
- `role`: user role (default `USER`)

The `User` model supports:
- `to_dict()` for database serialization
- `from_dict()` for deserialization

## Security Decisions

- Hashing algorithm: `bcrypt`
- Token type: JWT
- Token algorithm: `HS256`
- Token expiry: 1 hour
- Password requirements: minimum 8 characters, at least one letter, at least one number
- Storage: SQLite

## Configuration

The project supports environment-based secret configuration:

- `JWT_SECRET_KEY` — JWT signing secret

If unset, the default secret is `dev-secret-only`, intended only for development.

## Validation Rules

### Email

- Must not be empty
- Must match a standard email regular expression

### Password

- Minimum length: 8 characters
- Must include at least one numeric digit
- Must include at least one alphabetic character

## Components

### `core/auth.py`

Handles:
- user registration
- login
- credential verification

Registration workflow:
- validate email
- validate password
- ensure email is unique
- hash password
- create and persist a new user

Login workflow:
- retrieve user by email
- verify password
- generate JWT token on success

### `core/tokens.py`

Handles JWT creation and verification.

Token payload includes:
- `sub`: user id
- `email`
- `role`
- `iat`
- `exp`

If verification fails, it returns explicit failure reasons such as `Token expired` or `Invalid token`.

### `core/passwords.py`

Handles password hashing and verification using `bcrypt`.

### `storage/user_db.py`

Handles SQLite persistence using a `user` table with columns:
- `id`
- `email`
- `password_hash`
- `created_at`
- `role`

Supports:
- creating the table
- inserting users
- retrieving users by email or id
- checking whether an email exists

### `middleware/auth_middleware.py`

Provides a helper function `protect_route(token)` to validate a JWT and return user context.

## Error Handling

Common error flows include:
- invalid email format
- weak password
- duplicate email registration
- invalid login credentials
- expired or invalid JWT token

## Testing

Unit tests live in the `tests/` folder and should cover the auth flows, validators, storage, token handling, and middleware.

## Notes

- The project currently uses a local SQLite store and is suited for development or small-scale applications.
- For production, replace the default JWT secret and consider using a more robust persistence layer.
 - DESIGN DOCUMENT
