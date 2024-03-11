#!/usr/bin/python3

import unittest
from console import Console
from unittest.mock import patch

class TestConsole(unittest.TestCase):

    def test_quit_command(self):
        with patch('builtins.print') as mock_print:
            console = Console()
            result = console.onecmd('EOF')
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
