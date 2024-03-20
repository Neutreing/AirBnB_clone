#!/usr/bin/python3

import unittest
from console import Console
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """This is the unittest for the console file"""

    def test_quit_command(self):
        with patch('builtins.print') as mock_print:
            """test the code here"""
            console = Console()
            result = console.onecmd('EOF')
            self.assertTrue(result)

    def test_emptyline(self):
        """Test to check what happens when user inputs nothing"""
        with patch('builtins.print') as mock_print:
            console = Console()
            result = console.emptyline()
            self.assertIsNone(result)
            mock_print.assert_not_called()

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


if __name__ == "__main__":
    unittest.main()
