#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State"""

    def test_inherits_from_base_model(self):
        """Test that State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test that State has the expected attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of State"""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue(isinstance(state_dict["created_at"], str))
        self.assertTrue(isinstance(state_dict["updated_at"], str))
        self.assertTrue(isinstance(state_dict["id"], str))
        self.assertEqual(state_dict["name"], "")
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("id" in state_dict)
        self.assertTrue("name" in state_dict)

if __name__ == "__main__":
    unittest.main()

