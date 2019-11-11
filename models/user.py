#!/usr/bin/python3

from models.base_model import BaseModel

"""
Users module: inherits from BaseModel
"""


class User(BaseModel):
    """
    Class User to create an user
    Attributes
    ----------
    email: str
        User's email
    password: str
        User's password
    first_name: str
        User's first name
    last_name: str
        User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
