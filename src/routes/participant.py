from fastapi import APIRouter
from src.dtos.participants import ParticipantRegistrerDTO
from src.models.participant import Participant

router = APIRouter(
    prefix="/participant",
    tags=["participants"],
    responses={404: {"description": "Not Found"}}
)

@router.post("/")
async def register_participant(body: ParticipantRegistrerDTO):
    participant = await Participant.create(
        name = body.name,
        email = body.email
    )
    return {"participant": participant}

@router.get("/")
async def get_participants():
    participants = await Participant.all()
    return {"participants": participants}