from pydantic import BaseModel, EmailStr
from datetime import datetime

#---------------------------------
# Schema to Create User
#---------------------------------
class UserCreate(BaseModel):
    name: str 
    email: EmailStr
    password: str

#---------------------------------
# Schema to Create User
#---------------------------------
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime