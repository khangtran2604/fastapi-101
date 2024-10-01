from datetime import datetime

from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    created_at: datetime
    created_by: str
