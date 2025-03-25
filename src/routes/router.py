from fastapi import FastAPI
from src.routes import participant, group, users

def config_routes(app: FastAPI):
    app.include_router(participant.router)
    app.include_router(group.router)
    app.include_router(users.router)
