#!/usr/bin/python3
"""Unit tests for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""

    def test_inherits_from_base_model(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Test that Amenity has the expected attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of Amenity"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertTrue(isinstance(amenity_dict["created_at"], str))
        self.assertTrue(isinstance(amenity_dict["updated_at"], str))
        self.assertTrue(isinstance(amenity_dict["id"], str))
        self.assertTrue("created_at" in amenity_dict)
        self.assertTrue("updated_at" in amenity_dict)
        self.assertTrue("id" in amenity_dict)


if __name__ == "__main__":
    unittest.main()

