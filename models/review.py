#!/usr/bin/python3

from models.base_model import BaseModel

"""
Reviews module: inherits from BaseModel
"""


class Review(BaseModel):
    """
    Class Review to create an user
    Attributes
    ----------
    place_id: str
        Place's id (Place.id)
    user_id: str (User.id)
        User's id
    text: str
        Text to describe a review of the place
    """
    place_id = ""
    user_id = ""
    text = ""
