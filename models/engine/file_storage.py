#!/usr/bin/python3
"""File Storage"""
import json
from os import path


class FileStorage():
    """ FileStorage class"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns dictionary of object"""
        return FileStorage.__objects


    def new(self, obj):
        """ sets an object to create"""
        _id = obj.id
        key = str(obj.__class__.__name__) + "." + _id
        FileStorage.__objects[key] = obj


    def save(self):
        """Serialises to Json"""
        dicto = {}
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            for key, value in FileStorage.__objects.items():
                dicto[key] = value.to_dict()
            json.dump(dicto, file)


    def reload(self):
        """deserialises from Json"""
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fich:
                obj = json.load(fich)
                dicto = {}
                for cle, value in obj.items():
                    dicto[cle] = self.classes[value["__class__"]](**value)
                FileStorage.__objects = dicto
        else:
            return
