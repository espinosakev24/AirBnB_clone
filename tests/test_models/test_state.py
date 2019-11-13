#!/usr/bin/python3
"""
Unit test for State class
"""

from models.state import State
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestState(unittest.TestCase):
    """
    Test Cases for State
    """
    
    def setUp(cls):
        """
        Creating objests
        """
        # creating the objest
        cls.st = State()
        cls.st.name = "FLO"
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.st
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in state")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(State.__doc__)

    def test_issubclass(self):
        """
        Testing the construstor of the objest
        """
        self.assertTrue(issubclass(self.st.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.st.__dict__)
        self.assertIn('created_at', self.st.__dict__)
        self.assertIn('updated_at', self.st.__dict__)
        self.assertIn('name', self.st.__dict__)
        
    def test_save(self):
        """
        Test to save the information of State
        """
        self.st.save()
        self.assertNotEqual(self.st.created_at, self.st.updated_at)
        
    def test_to_dict(self):
        """
        Testing the dictionary created
        """
        self.assertEqual('to_dict' in dir(self.st), True)
        st_dict = self.st.to_dict()
        self.assertEqual(self.st.__class__.__name__, 'State')
        self.assertEqual(st_dict['__class__'], 'State')
        self.assertIsInstance(st_dict['created_at'], str)
        self.assertIsInstance(st_dict['updated_at'], str)
        self.assertIsInstance(st_dict['name'], str)
