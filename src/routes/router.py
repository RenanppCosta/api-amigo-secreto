from fastapi import FastAPI
from src.routes import participant, group

def config_routes(app: FastAPI):
    app.include_router(participant.router)
    app.include_router(group.router)
