from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from src.db.config import config_db
from src.routes.router import config_routes

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  
        allow_credentials=True,
        allow_methods=["*"],  
        allow_headers=["*"],  
    )

    config_db(app)
    config_routes(app)

    return app

app = create_app()