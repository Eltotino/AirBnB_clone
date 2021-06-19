#!/usr/bin/python3
"""FileStorage class"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    """FileStorage"""
    __file_path = "fichier.json"
    __objects = {}

    classes = {"BaseModel": BaseModel,
               "User": User}

    def all(self):
        """Returns a dictionary containing objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj with obj to be created"""
        _id = obj.id
        k = str(obj.__class__.__name__) + "." + _id
        FileStorage.__objects[k] = obj

    def save(self):
        """serialises object to json file"""
        dicto = {}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            for cle, valeur in FileStorage.__objects.items():
                dicto[cle] = valeur.to_dict()
            json.dump(dicto, file)

    def reload(self):
        """Deserialises json file to object"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                obj = json.load(file)
                dicto = {}
                FileStorage.__objects = dicto
        else:
            return
