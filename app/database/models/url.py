from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.config import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    name = Column("name", String)
    email = Column("email", String, unique=True)
    created_at = Column("created_at", DateTime, nullable=True)


class URL(Base):
    __tablename__ = "urls"
    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    long_url = Column("long_url", String)
    short_code = Column("short_code", String, unique=True)
    created_at = Column("created_at", DateTime, nullable=True)
