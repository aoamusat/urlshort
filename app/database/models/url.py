from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"
    id = Column("id", Integer, primary_key=True, autoincrement="auto")
    long_url = Column("long_url", String)
    short_code = Column("short_code", String, unique=True)
    created_at = Column("created_at", DateTime)
