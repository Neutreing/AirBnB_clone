#!/usr/bin/python3

import cmd
from models.entities import User


class Console(cmd.Cmd):
    """Creates the HBNB command ineterpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """This command is an EOF marker, which exits the program cleanly."""
        return True

    def emptyline(self):
        """This command disables repition on last command and does nothing."""
        pass

    def do_quit(self, line):
        """This command exits the interactive shell."""
        return True

    def register_create_profile_command(self):
        """Registers the CreateProfileCommand."""
        self.add_command("create_profiles", CreateProfileCommand)

    def do_create_profile(self, args):
        """Creats a new user profile"""
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        new_user = User(name, email, password)
        print("User profile created successfully: ")
        print(f"Name: {new_user.name}")
        print(f"Email: {new_user.email}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        Console().onecmd(' '.join(sys.argv[1:]))
    else:
        console = Console()
        console.cmdloop()
    print()
