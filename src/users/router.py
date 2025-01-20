from fastapi import APIRouter

from src.users.schemas import RegisterUserSchema
from src.users.service import UserService
from src.exceptions import (
    UserDoesNotExist
)

router = APIRouter(
    prefix="/authenticate",
    tags=["authenticate endponts"]
)

@router.post("/register")
async def register_user(
    user_data: RegisterUserSchema
):
    user = UserService.find_one_or_none(
        login=user_data.login
    )
    if user:
        raise UserDoesNotExist