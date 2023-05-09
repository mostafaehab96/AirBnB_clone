#!/usr/bin/python3

"""Defining the BaseModel class which is
the base class for all other classes.
"""

import datetime
import uuid
import models


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize the class with uniqe id."""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    time = datetime.datetime.fromisoformat(v)
                    setattr(self, k, time)
                else:
                    setattr(self, k, v)

    def __str__(self):
        """Returns string representation of the class."""
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the update_at attr with the current date and time."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        cls_dict = self.__dict__
        cls_dict["__class__"] = self.__class__.__name__
        cls_dict["created_at"] = self.created_at.isoformat()
        cls_dict["updated_at"] = self.updated_at.isoformat()
        return cls_dict
