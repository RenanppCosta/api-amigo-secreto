from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

def config_db(app: FastAPI):
    register_tortoise(
        app=app,
        config={
            "connections": {
                "default": "sqlite://db.sqlite3"
            },
            "apps": {
                "models": {
                    "models": [
                        "src.models.participant",
                        "src.models.group"
                    ],
                    "default_connection": "default",
                }
            },
        },
        generate_schemas=True,
        add_exception_handlers=True
    )
