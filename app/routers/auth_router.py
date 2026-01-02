from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/auth", tags=["Auth"])

service =  AuthService(UserRepository())

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    return service.login(data.email, data.password)