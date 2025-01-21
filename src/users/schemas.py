from pydantic import BaseModel, Field
from typing import Optional


class RegisterUserSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="User's full name")
    login: str = Field(
        ..., min_length=3, max_length=20, description="User's login name"
    )
    password: str = Field(
        ..., min_length=6, max_length=100, description="User's password"
    )
    tg_bot_token: Optional[str] = Field(None, description="Telegram bot token")
    tg_user_id: Optional[str] = Field(None, description="Telegram user ID")

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "login": "johndoe",
                "password": "strongpassword123",
                "tg_bot_token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
                "tg_user_id": "123456789",
            }
        }
