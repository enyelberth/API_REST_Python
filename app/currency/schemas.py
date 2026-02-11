from pydantic import BaseModel, EmailStr

#class UserBase(BaseModel):
 

class CurrencyCreate(BaseModel):
    name: str
    code:str
    description: str

class CurrencyResponse(BaseModel):
    id: int
    name: str
    code:str
 #   description: str
 #   uptated_at:str
 #   created_at:str