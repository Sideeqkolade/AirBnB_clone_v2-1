#!/usr/bin/python3
"""Defines the Database Storage Class"""
from sqlalchemy import create_engine
from os import environ, getenv
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# classes = {"User": User, "City": City, "State": State,
# "Place": Place, "Review": Review, "Amenity": Amenity}
classes = {"City": City, "State": State}


class DBStorage:
    """Database Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                   getenv('HBNB_MYSQL_DB')), pool_pre_ping=True
        )

        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        'all objects depending on the class name (argument cls)"""
        query_dict = {}

        if cls:
            objs = self.__session.query(cls)
            for obj in objs:
                query_dict[obj.__class__.__name__ + '.' + obj.id] = obj

        else:
            for key, value in classes.items():
                objs = self.__session.query(value)
                for obj in objs:
                    query_dict[obj.__class__.__name__ + '.' + obj.id] = obj

        return query_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()