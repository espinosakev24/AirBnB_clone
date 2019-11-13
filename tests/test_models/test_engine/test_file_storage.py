#!/bm/bin/python3
"""
Unit test for BaseModel class
"""

import json
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestBaseModel(unittest.TestCase):
    """
    Test Cases for BaseModel
    """
    
    def setUp(cls):
        """
        Creating objects
        """
        # creating the object
        cls.bm = BaseModel()
        cls.bm.name = "Kevin"
        cls.bm.age = 20
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.bm
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in base_model.py")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_methods(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_documentation(self):
        """
        Test to see if documentation is correct, created and not empty
        """
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.bm.__dict__)
        self.assertIn('created_at', self.bm.__dict__)
        self.assertIn('update_at', self.bm.__dict__)
        self.assertTrue(self.bm.id)

    def test_init(self):
        """
        Testing the constructor of the object
        """
        self.assertIsInstance(self.bm, BaseModel)
        
    def test_save(self):
        """
        Test to save the information of BaseModel
        """
        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.update_at)
        
    def test_to_dict(self):
        """
        Testing the dictionary created
        """
        bm_dict = self.bm.to_dict()
        self.assertEqual(self.bm.__class__.__name__, 'BaseModel')
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['update_at'], str)
