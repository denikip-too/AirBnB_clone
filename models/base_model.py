#!/usr/bin/python3
"""import modules"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """defines all common attributes/methods for other class"""

    def __init__(self, *args, **kwargs):
        """constructor of a class"""
        if kwargs is not None:
            my_dict = self.__dict__.copy()
            if 'created_at' in my_dict:
                my_dict['created_at'] = datetime.now()
            if 'updated_at' in my_dict:
                my_dict['updated_at'] = datetime.now()
            else:
                for key in kwargs:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        if 'created_at' in my_dict:
            time = datetime.now()
            my_dict['created_at'] = time.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in my_dict:
            time = datetime.now()
            my_dict['updated_at'] = time.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['__class__'] = type(self).__name__
        return my_dict

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
            self.__dict__))
