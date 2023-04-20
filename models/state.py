#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """ State class"""
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE")  == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    elif getenv("HBNB_TYPE_STORAGE") == 'file':
        name = ""
        @property
        def cities(self):
            city_list = []
            for key, value in models.storage.all().items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
