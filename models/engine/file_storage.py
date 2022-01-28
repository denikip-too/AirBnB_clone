#!/usr/bin/python3
"""import modules"""
import json


class FileStorage:
    """serializes instances to a JSON
    file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(FileStorage.__file_path, "r") as read_file:
            FileStorage.__objects = json.load(read_file)

    def classes(self):
        """imports classes from other directories and returns a dictionary"""
        from models.base_model import BaseModel
        from model.user import User
        from model.state import State
        from model.city import City
        from model.amenity import Amenity
        from model.place import Place
        from model.review import Review

        classes = {'BaseMobel': BasModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}
        return classes
