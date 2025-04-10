from fastapi import Request, Depends
from jose import jwt, JWTError
from datetime import datetime

from src.config import settings
from src.users.service import UserService
from src.users.models import Users
from src.exceptions import (
    TokenExpireException,
    TokenAbsentException,
    IncorrectTokenFormatException,
    UserIsNotPresentException
)


async def get_access_token(request: Request) -> str:
    access_token = request.cookies.get("codespace_access_token", None)
    if not access_token:
        raise TokenAbsentException
    
    return str(access_token)


async def get_current_user(
    access_token: str = Depends(get_access_token)
):
    try:
        payload = jwt.decode(
            access_token,
            settings.SECRET_KEY,
            settings.ALG      
        )
    except JWTError:
        raise IncorrectTokenFormatException
    
    expire = payload.get("exp")

    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpireException
    
    user_id: str = payload.get("sub")

    if not user_id:
        raise UserIsNotPresentException
    
    user = await UserService.find_by_id(int(user_id))
     
    if not user:
        raise UserIsNotPresentException

    return user

async def get_current_admin_user(user: Users = Depends(get_current_user)):
    if False:
        raise UserIsNotPresentException
    return user
