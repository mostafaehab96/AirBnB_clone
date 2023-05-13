#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects saved."""
        return FileStorage.__objects

    def new(self, obj):
        """Saves new created object in objects dict."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize saved objects into json file."""
        dict_to_save = {}
        for key, obj in FileStorage.__objects.items():
            dict_to_save[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_to_save, f)

    def reload(self):
        """Deserialize objects from json file."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**val)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
