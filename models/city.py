#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base, Column, String
from models import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False)
    name = Column(String(128),
                  ForeignKey(State.id, ondelete='CASCADE'), nullable=False)

    def __init__(self, obj_dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if obj_dict:
            for k, v in obj_dict.items():
                setattr(self, k, v)
        else:
            return        