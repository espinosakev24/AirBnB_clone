#!/usr/bin/python3
"""
Unit test for Amenity class
"""

from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestAmenity(unittest.TestCase):
    """
    Test Cases for Amenity
    """
    
    def setUp(cls):
        """
        Creating objects
        """
        # creating the object
        cls.am = Amenity()
        cls.am.name = "swimming pool"
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.am
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in amenity")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_issubclass(self):
        """
        Testing the constructor of the object
        """
        self.assertTrue(issubclass(self.am.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.am.__dict__)
        self.assertIn('created_at', self.am.__dict__)
        self.assertIn('updated_at', self.am.__dict__)
        self.assertIn('name', self.am.__dict__)
        
    def test_save(self):
        """
        Test to save the information of Amenity
        """
        self.am.save()
        self.assertNotEqual(self.am.created_at, self.am.updated_at)
        
    def test_to_dict(self):
        """
        Testing the dictionary created
        """
        self.assertEqual('to_dict' in dir(self.am), True)
        am_dict = self.am.to_dict()
        self.assertEqual(self.am.__class__.__name__, 'Amenity')
        self.assertEqual(am_dict['__class__'], 'Amenity')
        self.assertIsInstance(am_dict['created_at'], str)
        self.assertIsInstance(am_dict['updated_at'], str)
        self.assertIsInstance(am_dict['name'], str)
