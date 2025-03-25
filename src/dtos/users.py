from pydantic import BaseModel, EmailStr

class UserRegistrerDTO(BaseModel):
    name: str
    email: EmailStr
    password: str