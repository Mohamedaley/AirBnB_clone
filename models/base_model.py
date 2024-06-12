#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """The base model class is the main class"""
    def __init__(self, *args, **kwargs):
        """The initialization method"""

        if kwargs:
            for key, value in kwargs.items():
                if key != __class__:
                    setattr(self, key, value)
            if "created_at" or "updated_at" in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update the time of instance creation"""

        self.updated_at = datetime.today()

    def to_dict(self):
        """A function to collect the needed data and put them into dic
        by making a copy of __dict__ using {**self}"""

        temp = self.__dict__.copy()
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        return temp

    def __str__(self):
        """overriding the __str__ method to print specific format"""

        return "[{}] ({}) {}".format(type(self).
                                     __name__, self.id, self.__dict__)
