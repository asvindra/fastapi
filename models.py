from sqlalchemy import Column, Integer, String
from db import Base

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True,autoincrement = True)
    description = Column(String, unique=True, index=True)
    name = Column(String)
    priority = Column(Integer)
