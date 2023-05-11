#!/usr/bin/python3
"""Unit tests for City class"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City"""

    def test_inherits_from_base_model(self):
        """Test that City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test that City has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of City"""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertTrue(isinstance(city_dict["created_at"], str))
        self.assertTrue(isinstance(city_dict["updated_at"], str))
        self.assertTrue(isinstance(city_dict["id"], str))
        self.assertEqual(city_dict["state_id"], "")
        self.assertEqual(city_dict["name"], "")
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)
        self.assertTrue("id" in city_dict)
        self.assertTrue("state_id" in city_dict)
        self.assertTrue("name" in city_dict)

if __name__ == "__main__":
    unittest.main()

