#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """The storage engine in AirBnB project"""

    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        """The initialization method (Constructor)"""
        pass

    def all(self):
        """Return the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the __objects dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects stored and persists in file"""
        temp = {}
        for key, obj in FileStorage.__objects.items():
            temp[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """This method will deserialize the JSON
        string to a Python dictionary"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for key, value in new_obj_dict.items():
                    cls_name = key.split('.')[0]
                    if cls_name == 'BaseModel':
                        obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
