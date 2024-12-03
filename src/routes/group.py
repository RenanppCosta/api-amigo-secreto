from fastapi import APIRouter
from src.dtos.groups import GroupRegistrerDTO
from src.models.group import Group
router = APIRouter(
    prefix="/group",
    tags=["Groups"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def create_group(body: GroupRegistrerDTO):
    group = await Group.create(
        name = body.name,
        date = body.date
    )
    return {
        "id": group.id,
        "name": group.name,
        "date": group.formatted_date
    }

@router.get("/")
async def get_groups():
    groups = await Group.all().prefetch_related("participants") 
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
