from typing import Set

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str


    class Config:
        env_file = '.env'


settings = Settings()
