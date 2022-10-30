#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return (FileStorage.__objects)

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)'''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for obj_item in obj_dict.values():
                class_name = obj_item["__class__"]
                del obj_item["__class__"]
                self.new(eval(class_name)(**obj_item))
        except FileNotFoundError:
            pass

    def save(self):
        """ serializes __objects to the JSON file in __path"""

        j_objects = {}
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
        # Convert the dictionary into json and save in __filepath.
        with open(self.__file_path, 'w') as f:
            json.dump(j_objects, f)
