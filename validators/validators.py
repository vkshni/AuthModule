# Validate

from re import fullmatch


# Validate email
def validate_email(email: str):

    if not email or email.isspace():
        return (False, "Invalid email")

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not fullmatch(pattern, email):
        return (False, "Invalid email")

    return (True, "")


# Validate password
def validate_password(password: str):

    if len(password) < 8:
        return (False, "Short password (atleast 8 char)")

    if not any(c.isdigit() for c in password):
        return (False, "Password must contain atleast one number")

    if not any(c.isalpha() for c in password):
        return (False, "Password must contain atleast one letter")

    return (True, "")
