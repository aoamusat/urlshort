from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database.config import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    name = Column("name", String)
    email = Column("email", String, unique=True)
    created_at = Column("created_at", DateTime, nullable=True)

    urls = relationship('URL', back_populates='user')


class URL(Base):
    __tablename__ = "urls"
    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    long_url = Column("long_url", String)
    short_code = Column("short_code", String, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column("created_at", DateTime, nullable=True)

    user = relationship('User', back_populates='urls')