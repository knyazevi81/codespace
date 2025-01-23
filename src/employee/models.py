from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import List

from src.employee.logs.models import Logs
from src.database import Base

class Employees(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(nullable=False, default=True)
    codespace_id: Mapped[int] = mapped_column(ForeignKey("codespaces.id"), nullable=False)
    token: Mapped[str] = mapped_column(nullable=False)
    expire: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    #logs: Mapped[List["Logs"]] = relationship("Logs", back_populates="employee")

    class Config:
        from_attributes = True