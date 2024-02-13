#!/usr/bin/python3
"""a user class that inherits from the base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """defines a class user

    Attributes:
    email (str): email of the user.
    passowrd  (str): passowrd of user.
    first_name (str): name of the user.
    last_name (str): last name of the use.

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
