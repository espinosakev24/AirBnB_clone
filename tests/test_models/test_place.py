#!/usr/bin/python3
"""
Unit test for Place class
"""

from models.place import Place
from models.base_model import BaseModel
import os
import pep8
import unittest

class TestPlace(unittest.TestCase):
    """
    Test Cases for Place
    """
    
    def setUp(cls):
        """
        Creating objepls
        """
        # creating the object
        cls.pl = Place()
        cls.pl.name = "Coltejer"
        cls.pl.description = "Near to the Oriental Avenue"
        cls.pl.city_id = "4"
        cls.pl.users_id = "Kevin1"
        cls.pl.number_bathrooms = 2
        cls.pl.number_rooms = 3
        cls.pl.max_guest = 8
        cls.pl.price_by_nigth = 90
        cls.pl.latitude = 30.0
        cls.pl.longitude = 20.0
        cls.pl.amenity_ids = ["swimming pool", "gym"]

    def tearDown(cls):
        """
        Cleaning all
        """
        # cleaning the class
        del cls.pl
        # deleting the file
        if os.path.exists("file.json"):
            os.remove("file.json")
            
        
    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8 in place")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Place.__doc__)

    def test_issubclass(self):
        """
        Testing the construplor of the object
        """
        self.assertTrue(issubclass(self.pl.__class__, BaseModel), True)

    def test_attributes(self):
        """
        Testing the attributes of the class
        """
        self.assertIn('id', self.pl.__dict__)
        self.assertIn('created_at', self.pl.__dict__)
        self.assertIn('updated_at', self.pl.__dict__)
        self.assertIn('name', self.pl.__dict__)
        self.assertIn('city_id', self.pl.__dict__)
        self.assertIn('users_id', self.pl.__dict__)
        self.assertIn('description', self.pl.__dict__)
        self.assertIn('number_rooms', self.pl.__dict__)
        self.assertIn('number_bathrooms', self.pl.__dict__)
        self.assertIn('max_guest', self.pl.__dict__)
        self.assertIn('price_by_nigth', self.pl.__dict__)
        self.assertIn('latitude', self.pl.__dict__)
        self.assertIn('longitude', self.pl.__dict__)
        self.assertIn('amenity_ids', self.pl.__dict__)
        
    def test_save(self):
        """
        Test to save the information of Place
        """
        self.pl.save()
        self.assertNotEqual(self.pl.created_at, self.pl.updated_at)
        
    def test_to_dict(self):
        """
        Testing the diplionary created
        """
        self.assertEqual('to_dict' in dir(self.pl), True)
        pl_dipl = self.pl.to_dict()
        self.assertEqual(self.pl.__class__.__name__, 'Place')
        self.assertEqual(pl_dipl['__class__'], 'Place')
        self.assertIsInstance(pl_dipl['created_at'], str)
        self.assertIsInstance(pl_dipl['updated_at'], str)
        self.assertIsInstance(pl_dipl['name'], str)
        self.assertIsInstance(pl_dipl['number_rooms'], int)
        self.assertIsInstance(pl_dipl['number_bathrooms'], int)
        self.assertIsInstance(pl_dipl['max_guest'], int)
        self.assertIsInstance(pl_dipl['price_by_nigth'], int)
        self.assertIsInstance(pl_dipl['latitude'], float)
        self.assertIsInstance(pl_dipl['longitude'], float)
        self.assertIsInstance(pl_dipl['amenity_ids'], list)
