from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import List


from src.employee.logs.models import Logs
from src.database import Base


class Employess(Base):
    __tablename__ = "employess"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(nullable=False, default=True)
    codespace_id: Mapped[int] = mapped_column(ForeignKey("codespace.id"), nullable=False)
    token: Mapped[str] = mapped_column(nullable=False)
    expire: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    log: Mapped[List["Logs"]] = relationship(back_populates="logs")
