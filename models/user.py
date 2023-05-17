#!/usr/bin/python3
"""Define the User Class."""
from models.base_model import BaseModel

class user(BaseModel):
    """Represents a user.
    Attr:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
