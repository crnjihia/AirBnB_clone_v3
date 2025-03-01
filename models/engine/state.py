#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter method for cities if storage is not DBStorage"""
        from models.city import City
        if models.storage.__class__.__name__ != 'DBStorage':
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
        return []
