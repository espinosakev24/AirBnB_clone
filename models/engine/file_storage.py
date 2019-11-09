#!/usr/bin/python3
"""
FileStorage module
"""


import json
from models.base_model import BaseModel
import os.path

class FileStorage():
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        if obj:
            obj_class = type(obj).__name__
            self.__objects.update({str(obj_class + '.' + obj.id): obj})

    def save(self):
        """
        """
        with open(self.__file_path, 'w') as json_file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict.update({key: dict(value.to_dict())})
            json_file.write(json.dumps(new_dict))

    def reload(self):
        """
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                reload_obj = json.loads(json_file.read())
                for key, value in reload_obj.items():
                    self.__objects.update({key: BaseModel(**value)})
