from pydantic import BaseModel
from fastapi import HTTPException

def login_wrong():
    raise HTTPException(status_code=404, detail="E-mail ou Senha estão incorretos.")

def email_already_exist():
     raise HTTPException(status_code=409, detail="E-mail ja está cadastrado.")