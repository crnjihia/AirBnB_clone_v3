#!/usr/bin/python3
"""User module for the AirBnB clone project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import hashlib

class User(BaseModel, Base):
    """User class for representing users in the AirBnB clone.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = self._hash_password(kwargs['password'])

    def _hash_password(self, password):
        """Hash the password using MD5."""
        return hashlib.md5(password.encode()).hexdigest()

    def update_password(self, new_password):
        """Update the user's password and hash it."""
        self.password = self._hash_password(new_password)
        self.save()

    def to_dict(self, for_storage=False):
        """Convert User instance to dictionary."""
        user_dict = super().to_dict(for_storage)
        if for_storage:
            user_dict['password'] = self.password
        return user_dict
