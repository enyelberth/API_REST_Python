from pydantic import BaseModel, EmailStr

#class UserBase(BaseModel):
 

class CurrencyCreate(BaseModel):
    name: str
    code:str
    description: str

class CurrencyResponse(BaseModel):
    id: int
    active: bool = True