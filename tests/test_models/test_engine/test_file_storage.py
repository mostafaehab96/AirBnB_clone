#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Tear down test fixtures"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method"""
        # Create some test objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        # Save the objects
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        # Test that all() returns a dictionary with the correct objects
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)
        self.assertEqual(all_objs["BaseModel.{}".format(obj1.id)], obj1)
        self.assertEqual(all_objs["BaseModel.{}".format(obj2.id)], obj2)

    def test_new(self):
        """Test the new() method"""
        # Create a test object
        obj = BaseModel()
        # Test that new() adds the object to the __objects dictionary
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save(self):
        """Test the save() method"""
        # Create a test object
        obj = BaseModel()
        # Save the object
        self.storage.new(obj)
        self.storage.save()
        # Test that the file was created and contains the correct data
        with open(self.file_path, "r") as f:
            file_data = f.read()
            self.assertIn("BaseModel.{}".format(obj.id), file_data)
            self.assertIn("\"id\": \"{}\"".format(obj.id), file_data)

    def test_reload(self):
        """Test the reload() method"""
        # Create some test objects and save them to a file
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        # Reload the data from the file
        self.storage.reload()
        # Test that the objects were loaded correctly
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objs)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objs)
        self.assertEqual(all_objs["BaseModel.{}".format(obj1.id)].to_dict(), obj1.to_dict())
        self.assertEqual(all_objs["BaseModel.{}".format(obj2.id)].to_dict(), obj2.to_dict())

