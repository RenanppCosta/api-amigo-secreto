from fastapi import APIRouter, Depends
from src.dtos.groups import GroupRegistrerDTO
from src.models.group import Group
from src.models.user import User
from src.models.participant import Participant
from src.middlewares.auth import get_current_user

router = APIRouter(
    prefix="/group",
    tags=["Groups"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def create_group(body: GroupRegistrerDTO, user_logged: User = Depends(get_current_user)):

    new_group = await Group.create(
        created_by = user_logged,
        name = body.name,
        date = body.date
    )

    await Participant.create(
        name = user_logged.name,
        email = user_logged.email,
        group = new_group
    )

    return {
        "id": new_group.id,
        "name": new_group.name,
        "date": new_group.formatted_date,
        "created_by": new_group.created_by.name
    }

@router.get("/")
async def get_groups(user_logged: User = Depends(get_current_user)):
    groups = await Group.all().prefetch_related("participants").filter(created_by=user_logged)
    return [
        {
            "id": group.id,
            "name": group.name,
            "date": group.formatted_date,
            "participants": [
                {
                    "id": participant.id,
                    "name": participant.name,
                    "email": participant.email
                }
                for participant in group.participants
            ],
        }
        for group in groups
    ]
