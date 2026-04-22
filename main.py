# CLI Interface

from pathlib import Path
import sys
import argparse
from colorama import init, Fore

# Project modules
from core.auth import AuthService
from core.tokens import verify_token
from storage.user_db import UserDB

# Initialize
init(autoreset=True)
auth = AuthService(UserDB())

# UI Helpers
def print_success(msg):
    print(Fore.GREEN + f"✓ {msg}")

def print_error(msg):
    print(Fore.RED + f"✗ {msg}")

# COMMANDS

def cmd_register(args):
    try:
        success, data = auth.register(args.email, args.password)
        if success:
            print_success("User registered successfully")
            print(f"User ID: {data}")
        else:
            print_error(data)
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)

def cmd_login(args):
    try:
        success, data = auth.login(args.email, args.password)
        if success:
            print_success("Login successful!")
            print(f"Token: {data}")
        else:
            print_error(data)
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)

def cmd_verify(args):
    try:
        success, payload = verify_token(args.token)
        if success:
            print_success("Token valid")
            print(f"User ID: {payload.get('sub')}")
            print(f"Email: {payload.get('email')}")
            print(f"Role: {payload.get('role')}")
        else:
            print_error(payload)
    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)

# Main
def main():
    parser = argparse.ArgumentParser(
        prog="Auth Module",
        description="User authentication CLI"
    )
    
    sub = parser.add_subparsers(dest="command")

    # Register
    p_register = sub.add_parser("register", help="Register new user")
    p_register.add_argument("--email", required=True)
    p_register.add_argument("--password", required=True)

    # Login
    p_login = sub.add_parser("login", help="Login user")
    p_login.add_argument("--email", required=True)
    p_login.add_argument("--password", required=True)

    # Verify
    p_verify = sub.add_parser("verify", help="Verify token")
    p_verify.add_argument("token")

    # Help
    p_help = sub.add_parser("help", help="Show help")

    try:
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(0)
        
        args = parser.parse_args()

        if args.command == "register":
            return cmd_register(args)
        elif args.command == "login":
            return cmd_login(args)
        elif args.command == "verify":
            return cmd_verify(args)
        elif args.command == "help":
            parser.print_help()
            return 0

    except Exception as e:
        print_error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()