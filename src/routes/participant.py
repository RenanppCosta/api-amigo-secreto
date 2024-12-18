from fastapi import APIRouter, HTTPException
from src.dtos.participants import ParticipantRegistrerDTO
from src.models.participant import Participant
from src.models.group import Group
from src.utils.email import send_match_email
import random 

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

@router.patch("/{group_id}")
async def create_matches(group_id: int):
    group = await Group.get(id=group_id)

    list_id = []

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    participants = await Participant.filter(group=group).all()

    for participant in participants:
        list_id.append(participant.id)
    
    for participant in participants:
        matches = [pid for pid in list_id if pid != participant.id]

        match_id = random.choice(matches)

        match = await Participant.get(id=match_id)

        participant.match = match

        await participant.save()
        list_id.remove(match_id)

        await send_match_email(
            receiver_email=participant.email,
            participant_name=participant.name,
            match_name=participant.match.name,
            group_name=group.name,
            group_date=group.formatted_date
        )
   
    return {"matches": "Created Matches!"}

@router.get("{participant_id}/match")
async def get_match_by_participant(participant_id: int):
    participant = await Participant.get(id=participant_id).select_related("match", "group")

    await send_match_email(
            receiver_email=participant.email,
            participant_name=participant.name,
            match_name=participant.match.name,
            group_name=participant.group.name,
            group_date=participant.group.formatted_date
        )

    return{
        "match": participant.match.name
    }