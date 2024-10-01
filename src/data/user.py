from typing import Annotated
from uuid import uuid4

from fastapi import HTTPException, status

from data.init import curs
from dto.user import CreateUser
from error.user import UserAlreadyExists, UserNotFound
from helper.auth import LoginRequired
from helper.bcrypt import hash_password
from helper.jwt import decode
from model.user import User

assert curs is not None

init_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    fullname TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

curs.execute(init_table_sql)


def row_to_user(row: tuple) -> User:
    return User(id=row[0], username=row[1], fullname=row[2], password=row[3])

def create_user(create_data: CreateUser) -> User:
    exist_user = get_user_by_username(create_data.username)
    if exist_user is not None:
        raise UserAlreadyExists(f"User with username {create_data.username} already exists!")

    id = str(uuid4())
    username = create_data.username
    fullname = create_data.fullname
    password = hash_password(create_data.password)
    curs.execute(
        "INSERT INTO users (id, username, fullname, password) VALUES (?, ?, ?, ?)",
        (id, username, fullname, password)
    )

    return User(id=id, username=username, fullname=fullname, password=password)

def get_user_by_username(username: str) -> User | None:
    sql = "SELECT * FROM users WHERE username = :username"
    params = {"username": username}
    curs.execute(sql, params)
    row = curs.fetchone()
    return row_to_user(row) if row else None

async def get_current_user(token: LoginRequired) -> User:
    decoded_data = decode(token)
    username = decoded_data.get('sub')
    if username is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token was not found!")
        
    print(f"decoded_data.get('sub'): {username}")
    user = get_user_by_username(username)
    if not user:
        raise UserNotFound(f"User with username {username} not found!")
    return user
