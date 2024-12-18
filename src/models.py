import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla intermedia para la relación muchos a muchos entre personajes y naves espaciales
character_starship = Table('character_starship', Base.metadata,
    Column('character_id', Integer, ForeignKey('characters.id'), primary_key=True),
    Column('starship_id', Integer, ForeignKey('starships.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    description = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)
    description = Column(String(250), nullable=True)
    starships = relationship('Starships', secondary=character_starship, back_populates='pilots')

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    hyperdrive_rating = Column(String(10), nullable=True)
    starship_class = Column(String(50), nullable=False)
    pilots = relationship('Characters', secondary=character_starship, back_populates='starships')

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    classification = Column(String(50), nullable=False)
    average_height = Column(Integer, nullable=True)
    average_lifespan = Column(Integer, nullable=True)
    language = Column(String(50), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

    def to_dict(self):
        return {}

# Generar el diagrama
render_er(Base, 'diagram.png')

