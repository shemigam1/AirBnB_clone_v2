#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This class manages storage of hbnb models in DB format"""
    __engine = None
    __session = None
    
    def __init__(self):
        """initialization method"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """get all objects in db"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        class_list = []
        if cls == None:
            for subclass in Base.__subclasses__():
                class_list.extend(self.__session.query(subclass).all())
        else:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                class_list = self.__session.query(cls).all()
        class_dict = {}
        for item in class_list:
            key = f"{item.__class__.__name__}.{item.id}"
            class_dict[key] = item
        return class_dict
    
    def new(self, obj):
        """create new db instances"""
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session 
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """
        recreate all db instances"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()