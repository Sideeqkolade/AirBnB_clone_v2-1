#!/usr/bin/python3

"""
Storage
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchmemy.orm import sessionmaker
from models.base_model import Base
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {"User": User, "City": City, "State": State,
        "Place": Place, "Review": Review, "Amenity": Amenity}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:/3306/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))

        if getenv("HBNB_ENV") == 'test':
             Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        empty_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                empty_dict[key] = obj
            return empty_dict
        else:
            for key, value in classes.items():
                objs = self.__session.query(value).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    empty_dict[key] = obj
            return empty_dict
        
