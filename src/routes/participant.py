from fastapi import APIRouter, HTTPException
from src.dtos.participants import ParticipantRegistrerDTO
from src.models.participant import Participant
from src.models.group import Group

router = APIRouter(
    prefix="/participant",
    tags=["participants"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def register_participant(body: ParticipantRegistrerDTO):
    group = await Group.get(id= body.group)
    
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    participant = await Participant.create(
        name = body.name,
        email = body.email,
        group = group
    )

    return {"participant": {
        "id": participant.id,
        "name": participant.name,
        "email": participant.email,
        "group": participant.group.name 
    }}

@router.get("/{group_id}")
async def get_participants_by_group(group_id: int):
    group = await Group.get(id=group_id)

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    participants = await Participant.filter(group=group).all().select_related("group")

    return {
        "participants": [
            {
                "id": participant.id,
                "name": participant.name,
                "email": participant.email,
                "group": participant.group.name
            } for participant in participants
        ]
    }
