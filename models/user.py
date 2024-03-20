#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
#from models.base_model import Base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
