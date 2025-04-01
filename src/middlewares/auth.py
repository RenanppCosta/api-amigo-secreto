from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.utils.jwt import verify_access_token
from src.models.user import User

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = await User.get_or_none(email=payload.get("email"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
