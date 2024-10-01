from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

import data.user as service
from dto.auth import UserToken
from helper.bcrypt import verify_password
from helper.jwt import encode

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post('/login')
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = service.get_user_by_username(form_data.username)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Username or password is incorrect!")

    if not verify_password(form_data.password, user.password):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Username or password is incorrect!")
    return UserToken(access_token=encode({
        "sub": user.username,
    }), token_type="bearer")
