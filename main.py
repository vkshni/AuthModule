# CLI Interface

from pathlib import Path
import sys
import argparse


# Project modules
from core.auth import AuthService
from storage.user_db import UserDB


# Initialize auth
auth = AuthService(UserDB())

# COMMANDS

# Register
def cmd_register(args):

    try:
        success, error_msg = auth.register(args.email, args.password)
        if success:
            print("User registered successfully")
        else:
            print(error_msg)
    except Exception as e:
        print(e)
        sys.exit(1)

# Login
def cmd_login(args):

    try:
        success, error_msg = auth.login(args.email, args.password)
        if success:
            print(f"Token generated successfully: {error_msg}")
        else:
            print(error_msg)
    except Exception as e:
        print(e)
        sys.exit(1)



# Main
def main():

    # Argument Parser
    parser = argparse.ArgumentParser()

    sub = parser.add_subparsers(dest="command")

    # Register command
    p_register = sub.add_parser(name="register", help="Registers new users")
    p_register.add_argument("--email", type=str, required=True)
    p_register.add_argument("--password", type=str, required=True)

    # login command
    p_login = sub.add_parser(name="login", help="logs in users")
    p_login.add_argument("--email", type=str, required=True)
    p_login.add_argument("--password", type=str, required=True)

    try:

        if len(sys.argv) == 1:
            print("help")
            sys.exit(0)
        
        args = parser.parse_args()

        if args.command == "register":
            return cmd_register(args)
        
        elif args.command == "login":
            return cmd_login(args)

    except Exception as e:
        print(e)
        sys.exit(1)

main()

