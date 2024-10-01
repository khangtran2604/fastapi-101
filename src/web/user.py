from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

import data.user as service
from dto.user import CreateUser
from error.user import UserAlreadyExists

router = APIRouter(prefix="/user", tags=["user"])

@router.post('')
@router.post('/')
def create_user(body_data: Annotated[CreateUser, Body()]):
    try:
        return service.create_user(body_data)
    except UserAlreadyExists:
        return HTTPException(status_code=400, detail=f"User with username {body_data.username} already exists")

@router.get('/{username}')
def get_user(username: str):
        user = service.get_user_by_username(username)
        if not user:
            return HTTPException(status_code=404, detail=f"User with username {username} not found!")

        return user
