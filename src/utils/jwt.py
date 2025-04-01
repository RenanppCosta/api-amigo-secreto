import jwt
from jwt.exceptions import PyJWTError
from src.dtos.users import UserLoginDTO
from src.utils.config import settings
from datetime import datetime, timedelta


def create_access_token(data: UserLoginDTO):
    to_encode = data.model_dump()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except PyJWTError:
        return None