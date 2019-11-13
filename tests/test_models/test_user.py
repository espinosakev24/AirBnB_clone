#!/usr/bin/python3
"""
Unit test for User class
"""

from models.user import User
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestUser(unittest.TestCase):
    """
    Test Cases for User
    """
    
    def setUp(cls):
        """
        Creating objeusrs
        """
        # creating the objeusr
        cls.usr = User()
        cls.usr.email = "kevin@holbertonschool.com"
        cls.usr.password = "Happy123"
        cls.usr.first_name = "Kevin"
        cls.usr.last_name = "Espinosa"
        
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
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in user")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(User.__doc__)

    def test_issubclass(self):
        """
        Testing the construusror of the objeusr
        """
        self.assertTrue(issubclass(self.usr.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.usr.__dict__)
        self.assertIn('created_at', self.usr.__dict__)
        self.assertIn('updated_at', self.usr.__dict__)
        self.assertIn('email', self.usr.__dict__)
        self.assertIn('password', self.usr.__dict__)
        self.assertIn('last_name', self.usr.__dict__)
        self.assertIn('first_name', self.usr.__dict__)
        
    def test_save(self):
        """
        Test to save the information of User
        """
        self.usr.save()
        self.assertNotEqual(self.usr.created_at, self.usr.updated_at)
        
    def test_to_dict(self):
        """
        Testing the diusrionary created
        """
        self.assertEqual('to_dict' in dir(self.usr), True)
        usr_dict = self.usr.to_dict()
        self.assertEqual(self.usr.__class__.__name__, 'User')
        self.assertEqual(usr_dict['__class__'], 'User')
        self.assertIsInstance(usr_dict['created_at'], str)
        self.assertIsInstance(usr_dict['updated_at'], str)
        self.assertIsInstance(usr_dict['email'], str)
        self.assertIsInstance(usr_dict['password'], str)
        self.assertIsInstance(usr_dict['last_name'], str)
        self.assertIsInstance(usr_dict['first_name'], str)
