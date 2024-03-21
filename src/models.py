import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    is_admin = Column(Boolean, default=False)

class Film(Base):
    __tablename__ = 'film'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    director = Column(String(250))
    producer = Column(String(250))
    release_date = Column(String(250))
    opening_crawl = Column(String(500))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(50))
    gender = Column(String(50))
    height = Column(Integer)
    mass = Column(Numeric)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    skin_color = Column(String(50))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(Numeric)
    average_lifespan = Column(Integer)
    language = Column(String(100))
    homeworld = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    diameter = Column(Numeric)
    gravity = Column(String(50))
    population = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    surface_water = Column(Integer)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(Planet)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship(Character)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    film_id = Column(Integer, ForeignKey('film.id'))
    rating = Column(Integer)
    review_text = Column(String(500))
    user = relationship(User)
    film = relationship(Film)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Appearance(Base):
    __tablename__ = 'appearance'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    film_id = Column(Integer, ForeignKey('film.id'))
    character = relationship(Character)
    film = relationship(Film)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class CharacterSpecies(Base):
    __tablename__ = 'character_species'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    character = relationship(Character)
    species = relationship(Species)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
