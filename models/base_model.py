#!/usr/bin/python3
""" BaseModel moduel """
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class """
    def __init__(self, *args, **kwargs):
        """Constructor

        id (int) : public instance attribute

        """

        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """ str representation"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                  self.__dict__))

    def save(self):
        """update ublic instance aatirbute 'updated_at'"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionnary containing all k/v of the instance"""
        dictio = self.__dict__
        dictio["created_at"] = dictio["created_at"].isoformat()
        dictio["updated_at"] = dictio["updated_at"].isoformat()
        dictio["__class__"] = self.__class__.__name__
        return dictio
