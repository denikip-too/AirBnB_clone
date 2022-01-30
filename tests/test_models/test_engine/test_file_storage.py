#!/usr/bin/python3
"""import modules"""
import unittest
from models.base_model import BaseModel


class TestFileStorage(self):
    """test for class FileStorage"""

    def test_attributes(self):
        """tests common attributes/methods for other classes"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
