from fastapi import FastAPI
from src.db.config import config_db
from src.routes.router import config_routes

def create_app():
    app = FastAPI()

    config_db(app)
    config_routes(app)

    return app

app = create_app()

