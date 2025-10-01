import redis
from src.infrastructure.config.settings import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
    decode_responses=True,  # decode bytes to str
)
