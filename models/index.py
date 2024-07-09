from sqlalchemy import Table, Column, Integer, String
from config.db import meta

users = Table(
    'users', meta,
    Column('username', String, unique=True),
    Column('firstname', String),
    Column('lastname', String),
    Column('pincode', Integer),
    Column('email', String)
)
