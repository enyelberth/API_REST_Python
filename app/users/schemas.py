from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    id: int
    username: str
    email:str

class UserResponse(UserBase):
    id: int
    active: bool = True