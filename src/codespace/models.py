from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from typing import List

from src.employee.models import Employess
from src.database import Base

class Codespaces(Base):
    __tablename__ = "codespaces"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_name: Mapped[str] = mapped_column(nullable=False)
    encrypted_code: Mapped[str] = mapped_column(nullable=False)
    uuid: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = Mapped(ForeignKey("users.id"))

    employess: Mapped[List["Employess"]] = relationship(back_populates="employess")
