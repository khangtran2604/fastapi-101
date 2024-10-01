from typing import Annotated

from fastapi import APIRouter, Body, Depends

import data.product as service
from data.user import get_current_user
from dto.product import CreateProduct
from model.user import User

router = APIRouter(prefix="/product", tags=["product"])

@router.post('')
async def create_product(user: Annotated[User, Depends(get_current_user)], product_data: Annotated[CreateProduct, Body()]):
    return service.create_product(product_data, user.id)

@router.get('')
async def get_all_products( _: Annotated[User, Depends(get_current_user)]):
    return service.get_products()

@router.get('/{product_id}')
async def get_product_detail( product_id: str, _: Annotated[User, Depends(get_current_user)]):
    return service.get_product_by_id(product_id)
