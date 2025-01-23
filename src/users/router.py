from fastapi import APIRouter, Response

from src.users.schemas import RegisterUserSchema, UserAuthenticate
from src.users.service import UserService
from src.users.utils import authenticate_user, create_access_token, get_password_hash

from src.exceptions import (
    UserAlreadyExist,
    IncorrectLoginOrPasswordException
)

router = APIRouter(
    prefix="/authenticate",
    tags=["authenticate endponts"]
)

@router.post("/register")
async def register_user(
    user_data: RegisterUserSchema
):
    user = await UserService.find_one_or_none(
        login=user_data.login
    )
    if user:
        raise UserAlreadyExist
    
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(
        name=user_data.name,
        login=user_data.login,
        hashed_password=hashed_password
    )
    return None
    
@router.post("/login")
async def register_user(
    response: Response,
    user_data: UserAuthenticate
):
    user = await authenticate_user(
        login=user_data.login,
        password=user_data.password
    )
    if not user:
        raise IncorrectLoginOrPasswordException
    
    access_token = create_access_token({
        "sub": str(user.id)
    })

    response.set_cookie(
        "codespace_access_token",
        str(access_token),
        httponly=True
    )
    return access_token