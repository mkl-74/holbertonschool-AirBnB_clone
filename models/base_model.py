#!/usr/bin/python3
"""BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """create BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialized"""
        if kwargs:
            for key, value in kwargs.items():#check key, value
                if key != "__class__":#different of__class__
                    if key in ['created_at', 'updated_at']:
                       setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))#if key is 'created_at' or 'updated_at', we convert the value of the string to object 
                    else:
                       setattr(self, key, value)#for other key and value
        else:
            self.id = str(uuid.uuid4())#ID unique
            self.created_at = datetime.now()#Create
            self.updated_at = datetime.now()#update

    def __str__(self):
        """Print class, ID, Dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update instance with the date and hour"""
        self.updated_at = datetime.now()

    def to_dict(self):
        nw_dict = self.__dict__.copy()
        nw_dict['__class__'] = self.__class__.__name__
        nw_dict['created_at'] = self.created_at.isoformat()
        nw_dict['updated_at'] = self.updated_at.isoformat()
        return nw_dict
