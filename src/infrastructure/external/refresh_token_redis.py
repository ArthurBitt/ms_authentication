from src.infrastructure.external.redis_client import redis_client
from src.core.utils.date_handler import date_handler


def save_refresh_token(user_id: str, refresh_token: str, expire_days: int):
    redis_client.setex(
        name=f"refresh:{user_id}",
        time=date_handler.add_days(expire_days),
        value=refresh_token,
    )


def get_refresh_token(user_id: str):
    return redis_client.get(f"refresh:{user_id}")


def delete_refresh_token(user_id: str):
    redis_client.delete(f"refresh:{user_id}")
