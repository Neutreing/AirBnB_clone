#!/usr/bin/python3

import unittest
from models.users import User

class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

    def test_user_init(self):
        user = User("John Doe", "john@example.com", "password")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password")

if __name__ == "__main__":
    unittest.main()
