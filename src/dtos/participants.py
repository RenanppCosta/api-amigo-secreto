from pydantic import BaseModel, EmailStr

class ParticipantRegistrerDTO(BaseModel):
    name: str
    email: EmailStr
    group: int