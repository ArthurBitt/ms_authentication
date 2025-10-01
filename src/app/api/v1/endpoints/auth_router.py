from fastapi import APIRouter
from src.app.schemas.token import TokenRequest, TokenResponse
from src.app.services.token_service import TokenService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token", response_model=TokenResponse)
def generate_token(request: TokenRequest):
    tokens = TokenService.generate_tokens(request.user_id)
    return tokens
