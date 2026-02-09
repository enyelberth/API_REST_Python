from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    dni: str
    name: str
    second_name: Optional[str] = None
    username: str
    password: str
    email: str

class ItemBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    precio: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True