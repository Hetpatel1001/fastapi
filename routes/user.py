from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.user import User 


user = APIRouter()
@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{username}")
async def read_data(username:int):
    return conn.execute(users.select().where(users.c.username == username)).fetchall()

@user.post("/")
async def write_data(user:User):
    conn.execute(users.insert().velues(
        firstname=user.firstname,
        lastname=user.lastname,
        pincode=user.pincode,
        email=user.email
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/{username}")
async def update_data(username:int,user:User):
    conn.execute(users.update(
        firstname=user.firstname,
        lastname=user.lastname,
        pincode=user.pincode,
        email=user.email

    ).where(users.c.username == username))
    return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    conn.execute(users.delete(
        firstname=user.firstname,
        lastname=user.lastname,
        pincode=user.pincode,
        email=user.email
    ).where(users.c.username == username))
    return conn.execute(users.select())
