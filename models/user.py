#!/usr/bin/python3
"""import BaseModel"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class User:
    """class User attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
