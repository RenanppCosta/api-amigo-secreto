from pydantic import BaseModel

class GroupRegistrerDTO(BaseModel):
    name: str
    date: str
  