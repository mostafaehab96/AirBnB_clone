#!/usr/bin/python3
"""Unit tests for Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for Place"""

    def test_inherits_from_base_model(self):
        """Test that Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Test that Place has the expected attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_to_dict(self):
        """Test the to_dict method of Place"""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertTrue(isinstance(place_dict["created_at"], str))
        self.assertTrue(isinstance(place_dict["updated_at"], str))
        self.assertTrue(isinstance(place_dict["id"], str))
        self.assertEqual(place_dict["city_id"], "")
        self.assertEqual(place_dict["user_id"], "")
        self.assertEqual(place_dict["name"], "")
        self.assertEqual(place_dict["description"], "")
        self.assertEqual(place_dict["number_rooms"], 0)
        self.assertEqual(place_dict["number_bathrooms"], 0)
        self.assertEqual(place_dict["max_guest"], 0)
        self.assertEqual(place_dict["price_by_night"], 0)
        self.assertEqual(place_dict["latitude"], 0.0)
        self.assertEqual(place_dict["longitude"], 0.0)
        self.assertEqual(place_dict["amenity_ids"], [])
        self.assertTrue("created_at" in place_dict)
        self.assertTrue("updated_at" in place_dict)
        self.assertTrue("id" in place_dict)
        self.assertTrue("city_id" in place_dict)
        self.assertTrue("user_id" in place_dict)
        self.assertTrue("name" in place_dict)
        self.assertTrue("description" in place_dict)
        self.assertTrue("number_rooms" in place_dict)
        self.assertTrue("number_bathrooms" in place_dict)
        self.assertTrue("max_guest" in place_dict)
        self.assertTrue("price_by_night" in place_dict)
        self.assertTrue("latitude" in place_dict)
        self.assertTrue("longitude" in place_dict)
        self.assertTrue("amenity_ids" in place_dict)

if __name__ == "__main__":
    unittest.main()

