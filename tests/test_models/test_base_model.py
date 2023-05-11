#!/usr/bin/python3
"""test base model"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def test_init(self):
        """Test the __init__() method"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))
        self.assertTrue(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "updated_at"))

    def test_str(self):
        """Test the __str__() method"""
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """Test the save() method"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the to_dict() method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertTrue(isinstance(base_model_dict["created_at"], str))
        self.assertTrue(isinstance(base_model_dict["updated_at"], str))
        self.assertTrue(isinstance(base_model_dict["id"], str))

if __name__ == "__main__":
    unittest.main()

