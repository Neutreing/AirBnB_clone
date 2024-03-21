#!/usr/bin/python3
"""Defines unittests for console.py

Unittest classes:
    TestConsole_prompting
    TestConsole_exit
    TestConsole_create
"""

import unittest
import sys
from console import Console
from io import StringIO
from unittest.mock import patch


class TestConsole_prompting(unittest.TestCase):
    """Unittests for testing prompting of the command interpreter."""

    def test_emptyline(self):
        """Test to check what happens when user inputs nothing"""
        with patch('builtins.print') as mock_print:
            console = Console()
            result = console.emptyline()
            self.assertIsNone(result)
            mock_print.assert_not_called()

    def test_prompt_string(self):
        console = Console()
        self.assertEqual("(hbnb) ", console.prompt)


class TestConsole_exit(unittest.TestCase):
    """Unittests for testing exiting the command interpreter."""

    def test_quit_command(self):
        with patch('builtins.print') as mock_print:
            """test the code here"""
            console = Console()
            result = console.onecmd('EOF')
            self.assertTrue(result)

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(Console().onecmd("EOF"))


class TestConsole_create(unittest.TestCase):
    """Unittests for testing crested objects on the interpreter."""

    def test_create_profile_command(self):
        """
        Test creating a new user profile using
        the create_profile command.
        """
        with patch(
                'builtins.input', side_effect=['John', 'j@example.com', 'pass']
                ):
            with patch('builtins.print') as mock_print:
                console = Console()
                console.onecmd('create_profile')
                mock_print.assert_any_call(
                        "User profile created successfully: "
                        )
                mock_print.assert_any_call(f"Name: John")
                mock_print.assert_any_call(f"Email: j@example.com")


class TestConsole_help(unittest.TestCase):
    """Unittests for testing the help messages on the interpreter."""

    def test_help_quit(self):
        h = "This command exits the interactive shell."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(Console().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "This command is an EOF marker, which exits the program cleanly."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(Console().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
