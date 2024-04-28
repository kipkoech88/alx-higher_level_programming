#!/usr/bin/python3
""" City schema """
from model_state import Base, State
from sqlalchemy import String, Integer, Column, ForeignKey


class City(Base):
    """ City object schema """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
               autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
