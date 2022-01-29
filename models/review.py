#!/usr/bin/python3
"""import class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
