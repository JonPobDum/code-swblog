import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    usuario_ID = Column(Integer, primary_key=True)
    Nombre_usuario = Column(String(20))
    Nombre = Column(String(250), nullable=False)
    Apellido = Column(String(250), nullable=False)
    Correo = Column(String(250), nullable=False)

class Peliculas(Base):
    __tablename__ = 'Peliculas'
    Pelicula_ID = Column(Integer, primary_key=True)
    Nombre = Column(String(250), nullable=False )
    Trilogia = Column(String(50), nullable=True)
    Estreno = Column(Integer, nullable=False)

class Planetas(Base):
    __tablename__ = 'Planetas'
    Planeta_ID = Column(Integer, primary_key=True)
    Nombre_planeta= Column(String(50), nullable=False )
    Clima_planeta= Column(String(250), nullable=False)
    Poblacion= Column(Integer, nullable=False)
    diametro= Column(Integer, nullable=False)

class Personajes(Base):
    __tablename__ = 'Planetas'
    Personaje_ID = Column(Integer, primary_key=True)
    Nombre_personaje= Column(String(50), nullable=False )
    Lado_Fuerza= Column(String(250), nullable=False)
    Primera_Aparicion= Column(Integer, nullable=False)
    Estado = Column(Integer, nullable=False)

class Personajes_Favoritos(Base):
    __tablename__ = 'Personajes Favoritos'
    personaje_favorito_id = Column(Integer, primary_key=True)
    usuario_ID = Column(String(250), ForeignKey("Usuario.usuario_ID"))
    Personaje_ID = Column(Integer, ForeignKey("Personajes.Personaje_ID"))
    rel= relationship (Personajes)


class Planetas_Favoritos(Base):
    __tablename__ = 'Planetas Favoritos'
    Planetas_favoritos_id = Column(Integer, primary_key=True)
    usuario_ID = Column(String(250), ForeignKey ("Usuario.usuario_ID"))
    Planeta_ID = Column(Integer, ForeignKey ("Planetas.planeta_ID"))
    rel = relationship(Planetas)
    



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')