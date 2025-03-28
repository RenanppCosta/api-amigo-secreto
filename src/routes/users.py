from fastapi import APIRouter
from src.dtos.users import UserRegistrerDTO, UserLoginDTO
from src.models.user import User
from src.exceptions.user import login_wrong, email_already_exist
from src.utils.auth import hash_password, verify_password

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
    
    if user.password != body.password:
        return login_wrong()
    
    return user