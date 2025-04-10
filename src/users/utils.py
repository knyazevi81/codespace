from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

from src.config import settings
from src.users.service import UserService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_passsword: str) -> bool:
    pwd_context.verify(password, hashed_passsword)


def create_access_token(payload: dict[str, str]) -> str:
    to_encode = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=20)
    to_encode.update(
        {"exp": expire}
    )
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALG
    )
    return encoded_jwt

async def authenticate_user(login: str, password: str):
    user = await UserService.find_one_or_none(login=login)
    if not user and not verify_password(password, user.hashed_password): 
        return None
    return user
