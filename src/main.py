from fastapi import FastAPI
from src.db.config import config_db

def create_app():
    app = FastAPI()

    config_db(app)

    return app

app = create_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}