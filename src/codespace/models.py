from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import List

from src.employee.models import Employees
from src.database import Base

class Codespaces(Base):
    __tablename__ = "codespaces"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_name: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str] = mapped_column(nullable=False)
    public_access: Mapped[bool] = mapped_column(default=False)
    uuid: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    #employess: Mapped[List["Employees"]] = relationship(back_populates="employess")

    class Config:
        from_attributes = True
