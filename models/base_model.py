#!/usr/bin/python3
"""BaseModel"""


import uuid
import json
from models import storage
from datetime import datetime


class BaseModel:
    """create BaseModel"""
    __nb_objects = 0
    storage = None
    __objects = {}  # Empty dictionary
    tformat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """initialized"""
        if kwargs:
            for key, value in kwargs.items():  # check key, value
                if key != "__class__":  # different of__class__
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, BaseModel.tformat))  # noqa # # if key is 'created_at' or 'updated_at', w
                    else:
                        setattr(self, key, value)  # for other key and value
        else:
            BaseModel.__nb_objects += 1
            self.id = str(uuid.uuid4())  # ID unique
            self.created_at = datetime.now()  # Create
            self.updated_at = datetime.now()  # update
            if BaseModel.storage is not None:
                BaseModel.storage.new(self)

    def __str__(self):
        """Print class, ID, Dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update instance with the date and hour"""
        self.updated_at = datetime.now()
        BaseModel.__objects[self.id] = self.to_dict()
        if BaseModel.storage is not None:
            BaseModel.storage.save()  # call save self of storage

    def to_dict(self):
        """return dict"""
        nw_dict = self.__dict__.copy()
        nw_dict['__class__'] = self.__class__.__name__
        nw_dict['created_at'] = self.created_at.isoformat()
        nw_dict['updated_at'] = self.updated_at.isoformat()
        return nw_dict
