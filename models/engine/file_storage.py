import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    objs = json.load(f)
                    for key, value in objs.items():
                        cls_name = key.split('.')[0]
                        cls = globals().get(cls_name)
                        if cls:
                            self.__objects[key] = cls(**value)
                except json.JSONDecodeError:
                    pass
