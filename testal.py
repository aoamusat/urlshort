from sqlalchemy import create_engine, text, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey

metadata_obj = MetaData()

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/urlshorter", echo=True
)

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement="auto"),
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)
