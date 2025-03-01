#!/usr/bin/python3
"""DBStorage class definition"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects"""
        obj_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                obj_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for cls in [State, City]:
                for obj in self.__session.query(cls).all():
                    obj_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return obj_dict

    def new(self, obj):
        """Add object to session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.close()
