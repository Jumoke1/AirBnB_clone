#!/usr/bin/python3
"""a class place that inherits from the base model class"""
from models.base_models import BaseModel


class Place(BaseModel):
    """defines a class place
    Attribute:
        city_id (int): it will be the City.id
        user_id (int): it will be the User.id
        name(str): Name of the place
        description: Description of the place
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
