from fastapi import FastAPI
from src.routes import participant

def config_routes(app: FastAPI):
    app.include_router(participant.router)
