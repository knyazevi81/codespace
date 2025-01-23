from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from src.codespace.models import Codespaces
from src.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    tg_bot_token: Mapped[str | None]
    tg_user_id: Mapped[int | None]

    #codespaces: Mapped[List["Codespaces"]] = relationship()

    class Config:
        from_attributes = True
