#!/usr/bin/env python3

import uuid
import datetime

class BaseModel:
    """Base model of class """
    def __init__(self):
        """Initializee instance attributes id, created_at, and updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns class attributes in string format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of class attributes"""
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


