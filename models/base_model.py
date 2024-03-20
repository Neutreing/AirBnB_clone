#!/usr/bin/python

import uuid
from datetime import datetime


class BaseModel:
    """This defines all the common attributes/models for other classes"""

    def __init__(self):
        """Initialize the BaseModel, the base class for other models."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Method to represent an object as a string."""
        return "[{}] ({}) {}".format)self.__class__.__name__, self.id, self.__dict__)

