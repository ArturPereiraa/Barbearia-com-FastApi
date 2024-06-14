from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)  # Adicionando o campo senha diretamente

class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data = Column(Date)
    hora = Column(Time)

