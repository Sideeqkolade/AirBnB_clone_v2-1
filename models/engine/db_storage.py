#!/usr/bin/python3

"""
Storage
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
#from models.engine.file_storage



classes = {"User": User, "City": City, "State": State,
        "Place": Place, "Review": Review, "Amenity": Amenity}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"), pool_pre_ping=True))

        if getenv("HBNB_ENV") == 'test':
             Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        empty_dict = {}
        if cls:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                empty_dict[key] = obj
        else:
            for key, value in classes.items():
                objs = self.__session.query(value).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    empty_dict[key] = obj
        return empty_dict

    def new(self, obj):
        """
         add the object to the current database session (self.__session)
        """

        self.__session.add(obj)

    def save(self):
        """
         commit all changes of the current database session (self.__session)
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        #self.__session.commit()
        #self.save()
