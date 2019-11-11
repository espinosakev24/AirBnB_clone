#!/usr/bin/python3

from models.base_model import BaseModel

"""
State module: inherits from BaseModel
"""


class State(BaseModel):
    """
    Class State to create a state
    Attributes
    ----------
    name: str
        State's name
    """
    name = ""
