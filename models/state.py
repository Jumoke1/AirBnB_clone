#!/usr/bin/python3
""" class state that inherits from the BaseModel class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ defines a state class
    Attribute:
        name(str): name of the state
    """

    name = ""
