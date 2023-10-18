import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Favourite_Planet(Base):
    __tablename__ = 'favourite_planet'
        # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users = Column(String(50), unique=True)

class Favourite_Starship(Base):
    __tablename__ = 'favourite_starship'
        # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users = Column(String(50), unique=True)

class Favourite_Character(Base):
    __tablename__ = 'favourite_character'
        # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users = Column(String(50), unique=True)

    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    favourite_planet = Column(Integer, ForeignKey('favourite_planet.id'))
    favourite_planet_relationship = relationship(Favourite_Planet)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(50), unique=True)
    favourite_starship = Column(Integer, ForeignKey('favourite_starship.id'))
    favourite_starship_relationship = relationship(Favourite_Starship)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    height = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    created = Column(String(50))
    edited = Column(String(50))
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    favourite_character = Column(Integer, ForeignKey('favourite_character.id'))
    favourite_character_relationship = relationship(Favourite_Character)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    favourite_planet = Column(Integer, ForeignKey('favourite_planet.id'))
    favourite_planet_relationship = relationship(Favourite_Planet)
    favourite_starship = Column(Integer, ForeignKey('favourite_starship.id'))
    favourite_starship_relationship = relationship(Favourite_Starship)
    favourite_character = Column(Integer, ForeignKey('favourite_character.id'))
    favourite_character_relationship = relationship(Favourite_Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
