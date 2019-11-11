#!/usr/bin/python3

from models.base_model import BaseModel

"""
City module: inherits from BaseModel
"""


class City(BaseModel):
    """
    Class City to create a city
    Attributes
    ----------
    state_id: str
        State's id (State.id)
    name: str
        City's name
    """
    state_id = ""
    name = ""
