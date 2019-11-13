#!/usr/bin/python3
"""
Unit test for Review class
"""

from models.review import Review
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestReview(unittest.TestCase):
    """
    Test Cases for Review
    """
    
    def setUp(cls):
        """
        Creating objerevs
        """
        # creating the objerev
        cls.rev = Review()
        cls.rev.text = "Good place and view"
        
    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.rev
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in review")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Review.__doc__)

    def test_issubclass(self):
        """
        Testing the construrevor of the object
        """
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.rev.__dict__)
        self.assertIn('created_at', self.rev.__dict__)
        self.assertIn('update_at', self.rev.__dict__)
        self.assertIn('text', self.rev.__dict__)
        
    def test_save(self):
        """
        Test to save the information of Review
        """
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.update_at)
        
    def test_to_dict(self):
        """
        Testing the direvionary created
        """
        self.assertEqual('to_dict' in dir(self.rev), True)
        rev_direv = self.rev.to_dict()
        self.assertEqual(self.rev.__class__.__name__, 'Review')
        self.assertEqual(rev_direv['__class__'], 'Review')
        self.assertIsInstance(rev_direv['created_at'], str)
        self.assertIsInstance(rev_direv['update_at'], str)
        self.assertIsInstance(rev_direv['text'], str)
