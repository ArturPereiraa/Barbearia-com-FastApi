<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Date, Time
=======
# /app/models/models.py

from sqlalchemy import Column, Integer, String
>>>>>>> b82a2abc6a6776dc757eb49add006919d9138603
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

<<<<<<< HEAD
class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    data = Column(Date)
    hora = Column(Time)
=======
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
>>>>>>> b82a2abc6a6776dc757eb49add006919d9138603
