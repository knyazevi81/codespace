from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Mapped[int] = mapped_column(primary_key=True)
    name = Mapped[str] = mapped_column(nullable=False)
    hashed_password = Mapped[str] = mapped_column(nullable=False)
    tg_bot_token = Mapped[str]
    tg_user_id = Mapped[int]