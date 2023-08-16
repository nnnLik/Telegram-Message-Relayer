from typing import List
from decouple import config


SECRET_KEY: str = config("SECRET_KEY")
DEBUG: bool = config("DEBUG", cast=bool)

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=lambda v: [host for host in v.split(",") if host]
)
CORS_ORIGIN_WHITELIST: List[str] = config(
    "CORS_ORIGIN_WHITELIST",
    cast=lambda v: [origin.strip() for origin in v.split(",") if origin],
)

DB_ENGINE: str = config("DB_ENGINE")
DB_NAME: str = config("DB_NAME")
DB_USER: str = config("DB_USER")
DB_PASSWORD: str = config("DB_PASSWORD")
DB_HOST: str = config("DB_HOST")
DB_PORT: int = config("DB_PORT")
