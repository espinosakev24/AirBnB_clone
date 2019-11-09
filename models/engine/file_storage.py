#!/usr/bin/python3
"""
"""


import json
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
            obj_dict = obj.to_dict()
            obj_key = obj_dict['__class__'] + '.' + obj_dict['id']
            self.__objects[obj_key] = obj_dict

    def save(self):
        """
        """
        with open(self.__file_path, 'w') as json_file:
            json_file.write(json.dumps(self.__objects))

    def reload(self):
        """
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.loads(json_file.read())
