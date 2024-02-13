#!/usr/bin/python3
"""The BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """It defines the base model class"""

    def __init__(self, *args, **kwargs):
        """intialize the instace of a class"""
        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    time_obj = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time_obj)
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """update the instanve of a class"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """change to dictionary representation format"""
        obj_dict = (self.__dict__).copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """return the string representation"""
        string_rep = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return string_rep
