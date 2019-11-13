#!/usr/bin/python3
"""
Unit test for FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import all_classes
import os
import pep8
import unittest

class TestFileStorage(unittest.TestCase):
    """
    Test Cases for FileStorage
    """
    
    def setUp(cls):
        """
        Creating objects
        """
        # creating the object
        cls.usr = User()
        cls.usr.first_name = "Kevin"
        cls.usr.last_name = "Espinosa"
        cls.usr.email = "916@holbertonschool.com"
        cls.storage = FileStorage()
        cls.path = "file.json"
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.usr
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in file_storage.py")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_methods(self):
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_documentation(self):
        """
        Test to see if documentation is correct, created and not empty
        """
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_file_path(self):
        """
        Test to see if the file_self.path exist
        """
        self.assertEqual(FileStorage._FileStorage__file_path, self.path)

    def test_objects_exist_storage(self):
        """
        Test if __objects exist and was created
        """
        dic = self.storage.all()
        self.assertEqual(FileStorage._FileStorage__objects, dic)
        self.assertTrue(FileStorage._FileStorage__objects)

    def test_all(self):
        """
        Testing the method all
        """
        fl_storage = FileStorage()
        dic = fl_storage.all()
        self.assertIsNotNone(dic)
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, fl_storage._FileStorage__objects)

    def test_new(self):
        """
        Testing the new method
        """
        fl_storage = FileStorage()
        dic = fl_storage.all()
        usr1 = User()
        usr1.id = 1234
        usr1.name = "Daniela"
        fl_storage.new(usr1)
        usr_key = usr1.__class__.__name__ + '.' + str(usr1.id)
        self.assertIsNotNone(dic[usr_key])

    def test_save(self):
        """
        Testing the save method
        """
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists(self.path))
        bm.name = "Testing"
        bm.number = 1
        bm.save()
        self.assertTrue(os.path.exists(self.path))
        dic = {}
        with open('file.json', 'r') as fjson:
            dic = json.loads(fjson.read())
        bm_key = bm.__class__.__name__ + '.' + bm.id
        self.assertDictEqual(bm.to_dict(), dic[bm_key])

    def test_reload(self):
        """
        Testing the reload method
        """
        fl_storage = FileStorage()
        bm = BaseModel()
        bm.name = "Testing"
        bm.number = 2
        bm.save()
        ct = City()
        ct.name = "Medellin"
        ct.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertTrue(all_objs)
