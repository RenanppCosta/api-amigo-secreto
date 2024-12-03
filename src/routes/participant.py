from fastapi import APIRouter

router = APIRouter(
    prefix="/participant",
    tags=["participants"],
    responses={404: {"description": "Not Found"}}
)

@router.get("/")
async def home():
    return {"status": "Ok"}