#!/usr/bin/python3

import json
import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """Base model of class """
    def __init__(self, *args, **kwargs):
        """Initializee instance attributes id, created_at, and updated_at"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)

        else:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """Returns class attributes in string format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with current time and saves object"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of  attributes"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def save_json_to_file(self, filename):
        '''Saves instance of BaseModel to a file'''
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)


    def load_json_from_file(filename):
        '''loads an instance of BaseModel from a file'''
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
