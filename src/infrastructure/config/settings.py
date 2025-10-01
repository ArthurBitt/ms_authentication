from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = "supersecret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    DNS: str = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"

    model_config = SettingsConfigDict()

settings = Settings()

