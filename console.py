#!/usr/bin/python3

import cmd


class Console(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """This command is an EOF marker, which exits the program cleanly."""
        return True

    def emptyline(self):
        pass

    def do_quit(self, line):
        """This command exits the interactive shell."""
        return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        Console().onecmd(' '.join(sys.argv[1:]))
    else:
        Console().cmdloop()
    print()
