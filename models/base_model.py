#!/usr/bin/python
"""Defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """This defines all the common attributes/models for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    try:
                        setattr(self, key, datetime.syrptime(value, tform))
                    except ValueError:
                        print(f"Invalid datetime format for {key}: {value}")
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Method to represent an object as a string."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Method to update the 'updated_at' attribute
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method to return a dictionary representation of an object"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.created_at.isoformat()
        return dict_copy
