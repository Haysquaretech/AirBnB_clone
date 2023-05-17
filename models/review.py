#!/usr/bin/python3
"""Define the Review Class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review.
    Attr:
        place_id (str): The Place  id.
        user_id (str): The User id.
        text (str): The text of thte review.
    """
    place_id = ""
    user_id = ""
    text = ""
