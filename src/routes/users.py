from fastapi import APIRouter, Depends
from src.dtos.users import UserRegistrerDTO, UserLoginDTO
from src.models.user import User
from src.exceptions.user import login_wrong, email_already_exist
from src.utils.auth import hash_password, verify_password
from src.utils.jwt import create_access_token
from src.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def register_user(body: UserRegistrerDTO):
    
    email_exist = await User.filter(email=body.email)

    if email_exist:
        return email_already_exist()
    
    hashed_password = hash_password(body.password)

    user = await User.create(
        name = body.name,
        email = body.email,
        password = hashed_password
    )

    return {"user": {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }}
      
@router.post("/login")
async def login(body: UserLoginDTO):
    try:
        user = await User.get(email=body.email)
    except Exception:
        return login_wrong()
    
    if verify_password(body.password, user.password):
        return login_wrong()
    
    token = create_access_token(body)
    return {"token": token, "token_type": "bearer"}

@router.get("/me")
async def get_logged_user(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "name": current_user.name, "email": current_user.email}