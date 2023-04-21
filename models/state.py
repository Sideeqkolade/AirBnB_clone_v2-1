#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Column, String, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            city_list = []
            for key, value in models.storage.all().items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
