from fastapi import APIRouter
from src.dtos.users import UserRegistrerDTO
from src.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def register_user(body: UserRegistrerDTO):
    user = await User.create(
        name = body.name,
        email = body.email,
        password = body.password
    )

    return {"user": {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }}