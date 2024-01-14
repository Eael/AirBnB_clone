#!/usr/bin/env python3
"""Define the base model class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class for the airbnb clone"""

    def __init__(self, *args, **kwargs):
        """Initialises  a new BaseModel
        Args:
            *args(any): unsused
            **kwargs: key/value pairs of attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = strptime(v, time_form)
                else:
                    self.__dict__[k] = v

    def save(self):
        """updates the updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        including a key __class__ and value being the name of
        the object
        """

        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__
        return ndict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        clname = self.__class__.__name__
        print(f"[{clname}] ({self.id}) ({self.__dict__})")
