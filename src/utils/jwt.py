import jwt
from src.dtos.users import UserLoginDTO
from src.utils.config import settings


def create_access_token(data: UserLoginDTO):
    to_encode = data.model_dump()
    to_encode.update({"exp": "24h"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)