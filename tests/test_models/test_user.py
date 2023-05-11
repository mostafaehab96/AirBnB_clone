#!/usr/bin/python3
"""Unit tests for User class"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User"""

    def test_inherits_from_base_model(self):
        """Test that User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test that User has the expected attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of User"""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertTrue(isinstance(user_dict["created_at"], str))
        self.assertTrue(isinstance(user_dict["updated_at"], str))
        self.assertTrue(isinstance(user_dict["id"], str))
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)
        self.assertTrue("id" in user_dict)
        self.assertTrue("email" in user_dict)
        self.assertTrue("password" in user_dict)
        self.assertTrue("first_name" in user_dict)
        self.assertTrue("last_name" in user_dict)

if __name__ == "__main__":
    unittest.main()

