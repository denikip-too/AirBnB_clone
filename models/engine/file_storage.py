#!/usr/bin/python3
"""import modules"""
import json
import datetime
import os


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
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            d = {i: j.to_dict() for i, j in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as read_file:
            object_dict = json.load(read_file)
            object_dict = {i: self.classes()[j["__class__"]](**j) 
                       for i, j in object_dict.items()}
            FileStorage.__objects = object_dict

    def classes(self):
        """imports classes from other directories and returns a dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}
        return classes
