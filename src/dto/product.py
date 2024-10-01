from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
