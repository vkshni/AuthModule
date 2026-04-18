# JWT Tokens

import jwt
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Adding PROJECT ROOT to the Python Path
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Projec modules
from models.user import User


# Secret key
SECRET_KEY = "38a9ad42fb2e781ff53455dc0be3d4d62bb31cfcdb23b0204217a3bebf718a7e"


# Generate token
def generate_token(user: User):

    now = datetime.now(tz=timezone.utc)

    payload = {
        "sub": user.id,
        "email": user.email,
        "role": user.role,
        "iat": now,
        "exp": now + timedelta(hours=1),
    }
    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    except:
        return False


# Verify token
def verify_token(token):

    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return False


if __name__ == "__main__":

    u1 = User("vks@gmail.com", "3290jdsfkjds39sjklfjslf")

    token = generate_token(u1)
    print(token)
    decoded = verify_token(token)
    print(decoded)
