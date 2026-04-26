# Middleware

from pathlib import Path
import sys

# Adding PROJECT ROOT to the Python Path
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Project modules
from core.tokens import verify_token


def protect_route(token):

    # Extracting token
    is_valid, decoded = verify_token(token)

    if not is_valid:
        return (False, decoded)

    return (True, {"user_id": decoded.get("sub"), "role": decoded.get("role")})
