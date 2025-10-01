# third party
from jose import jwt

# local
from src.infrastructure.config.settings import settings
from src.core.utils.date_handler import date_handler


def create_access_token(payload: dict):
    expire = date_handler.add_minutes(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def create_refresh_token(user_id: str):
    expire = date_handler.add_days(settings.REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {"user_id": user_id, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
