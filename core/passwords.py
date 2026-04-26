# Password Hashing/Verification

# Libraries
from bcrypt import gensalt, hashpw, checkpw


# Hashing
def hash_password(plain_password: str) -> str | bool:

    try:
        hashed = hashpw(plain_password.encode(), gensalt())
        return hashed.decode()
    except:
        return False


# Verification
def verify_password(plain_password: str, hashed: str) -> bool:

    try:
        return checkpw(plain_password.encode(), hashed.encode())
    except:
        return False


if __name__ == "__main__":
    hashed = hash_password("vks")
    print(hashed)
    print(verify_password("vks", hashed))
