#!/usr/bin/python3

from models.base_model import BaseModel

"""
Place module: inherits from BaseModel
"""


class Place(BaseModel):
    """
    Class Place to create an user
    Attributes
    ----------
    city_id: str
        Where is the city of the place (Place.id)
    user_id: str
        User's id (User.id)
    name: str
        Place's name
    description: str
        Place's description
    number_rooms: int
        Number of rooms of the place
    number_bathrooms: int
        Number of bathrooms of the place
    max_guest: int
        Maximum number of guest
    price_by_night: int
        Price by nigth
    latitude: double
        Location of the place
    longitude: double
        Location of the place
    amenity_ids: list(str)
        Amenity's id (Amenity.id)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
