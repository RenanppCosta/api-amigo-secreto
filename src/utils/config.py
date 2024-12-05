from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configurações de SMTP
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_EMAIL: str 
    SMTP_PASSWORD: str 

    class Config:
        env_file = ".env"  # Carrega credenciais do arquivo .env

settings = Settings()
