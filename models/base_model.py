#!/usr/bin/python
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """This defines all the common attributes/models for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        # else:
            # models.storage.new(self)

    def save(self):
        """
        Method to update the 'updated_at' attribute
        with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Method to return a dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.created_at.isoformat()
        return dict_copy

    def __str__(self):
        """Method to represent an object as a string."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
