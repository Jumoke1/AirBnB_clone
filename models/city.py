#!/usr/bin/python3
""" class city that inherits from Basemodels"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines a city class
    Attributes:
        state_id (str): state id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
