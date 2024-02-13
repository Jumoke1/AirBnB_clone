#!/usr/bin/python3
""" class amenity that inherits from the BaseModel class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines the class amenities
    Attributes: name of the amenity
    """

    name = ""
