from pydantic import field_validator
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

    @field_validator("*", mode="before")
    @classmethod
    def strip_quotes(cls, v):
        """Убирает обёртывающие кавычки (Docker --env-file передаёт их в значении)."""
        if isinstance(v, str) and len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
            return v[1:-1]
        return v

settings = Settings()