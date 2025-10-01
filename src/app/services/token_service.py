from src.infrastructure.external.token_provider import create_access_token, create_refresh_token
from src.infrastructure.external.refresh_token_redis import save_refresh_token
from src.infrastructure.config.settings import settings


class TokenService:

    @staticmethod
    def generate_tokens(user_id: str):
        access_token = create_access_token({"sub": user_id})
        refresh_token = create_refresh_token(user_id)

        save_refresh_token(user_id, refresh_token, settings.REFRESH_TOKEN_EXPIRE_DAYS)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
