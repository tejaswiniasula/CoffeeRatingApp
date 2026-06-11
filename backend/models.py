from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Coffee(Base):

    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    description = Column(String)

    image = Column(String)

    votes = Column(Integer, default=0)