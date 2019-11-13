#!/usr/bin/python3
"""
Unit test for City class
"""

from models.city import City
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestCity(unittest.TestCase):
    """
    Test Cases for City
    """
    
    def setUp(cls):
        """
        Creating objects
        """
        # creating the object
        cls.ct = City()
        cls.ct.name = "MIA"
        cls.state_id = "FLO"
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.ct
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in city")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(City.__doc__)

    def test_issubclass(self):
        """
        Testing the constructor of the object
        """
        self.assertTrue(issubclass(self.ct.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.ct.__dict__)
        self.assertIn('created_at', self.ct.__dict__)
        self.assertIn('update_at', self.ct.__dict__)
        self.assertIn('name', self.ct.__dict__)
        
    def test_save(self):
        """
        Test to save the information of City
        """
        self.ct.save()
        self.assertNotEqual(self.ct.created_at, self.ct.update_at)
        
    def test_to_dict(self):
        """
        Testing the dictionary created
        """
        self.assertEqual('to_dict' in dir(self.ct), True)
        ct_dict = self.ct.to_dict()
        self.assertEqual(self.ct.__class__.__name__, 'City')
        self.assertEqual(ct_dict['__class__'], 'City')
        self.assertIsInstance(ct_dict['created_at'], str)
        self.assertIsInstance(ct_dict['update_at'], str)
        self.assertIsInstance(ct_dict['name'], str)
