from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    TOKEN_OPNEAI: str
    TOKEN_TG: str
    DB_CONNECT: str
    DB_NAME: str
    GEMINI_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
