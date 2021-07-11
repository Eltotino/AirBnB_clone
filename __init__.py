#!/usr/bin/python3
"""BaseModel Module"""
import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class"""
    def __init__(self):
        format_time = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Str format"""
        return "[{}] ({}) ({})".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
    """ Changes the instance updated_at"""
    self.updated_at = datetime.now()

    def to_dict(self):
    	"""Dictionary format"""
        dicto = dict(self.__dict__)
        dicto["created_at"] = dicto["created_at"].isoformat()
        dicto["updated_at"] = dicto["updated_at"].isoformat()
        dicto["__class__"] = self.__class__.__name__
        return dicto
