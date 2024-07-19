#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            get cities"""
            import models
            from models.city import City
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list