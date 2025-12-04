# core/config.py

from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
print("Base directory:", BASE_DIR)

class Settings(BaseSettings):
    # Application settings
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Database settings
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "mydatabase"

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
