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
        with patch('builtins.print') as mock_print:
            console = Console()
            result = console.emptyline()
            self.assertIsNone(result)
            mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
