#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.orm import declarative_base
import models

Base = declarative_base()
class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    # def to_dict(self):
    #     """Convert instance into dict format"""
    #     dictionary = {}
    #     dictionary.update(self.__dict__)
    #     dictionary.update({'__class__':
    #                       (str(type(self)).split('.')[-1]).split('\'')[0]})
    #     dictionary['created_at'] = self.created_at.isoformat()
    #     dictionary['updated_at'] = self.updated_at.isoformat()
    #     return dictionary
    
    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dict_copied = self.__dict__.copy()
        dict_copied["__class__"] = self.__class__.__name__
        dict_copied["created_at"] = self.created_at.isoformat()
        dict_copied["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dict_copied:
            del dict_copied["_sa_instance_state"]
        return dict_copied
    
    def delete(self):
        """delete the current instance from the storage (models.storage)
        by calling the method delete"""
        models.storage.delete(self)
    
