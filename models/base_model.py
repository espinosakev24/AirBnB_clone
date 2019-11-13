#!/usr/bin/python3
from datetime import datetime
import models
from uuid import uuid4
""" Module of base_model file
"""


class BaseModel():
    """BaseModel class: parent class of all child classes
    """
    def __init__(self, *args, **kwargs):
        """Constructor of BaseModel
        Attributes
        ----------
        *args: list
            argument list (not used)
        **kwargs: dict
            dictionary of arguments to create an object
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'update_at':
                    self.update_at = datetime.strptime(value,
                                                       '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Method to return a string representation of the class
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """
        Method that updates the public instance attribute updated_at with the
        current datetime and send to save in a JSON file
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        class_dict = self.__dict__.copy()
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': datetime.isoformat(self.created_at)})
        class_dict.update({'update_at': datetime.isoformat(self.update_at)})
        return class_dict
