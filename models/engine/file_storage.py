#!/usr/bin/python3
"""
FileStorage module
"""


import json
import models
import os.path


class FileStorage():
    """
    FileStorage class that serializes and deserializes a JSON file
    to instances
    Attributes:
    ----------
    -file_path: str
        save the path of the JSON file
    -objects:
        save a dictionary with the objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public method that returns a dictionary with all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Public method that sets in __objects a new object
        """
        if obj:
            obj_class = type(obj).__name__
            self.__objects.update({(obj_class + '.' + str(obj.id)): obj})

    def save(self):
        """
        Public method that serialize and save to a JSON file
        """
        with open(self.__file_path, 'w') as json_file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict.update({key: dict(value.to_dict())})
            json_file.write(json.dumps(new_dict))

    def reload(self):
        """
        Public method that deserialize a JSON file and save in __objects
        if the file exist
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                reload_obj = json.loads(json_file.read())
                for key, value in reload_obj.items():
                    obj_class = key.split('.')[0]
                    obj = models.all_classes[obj_class](**value)
                    self.__objects.update({key: obj})
