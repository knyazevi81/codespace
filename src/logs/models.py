from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from datetime import date

from src.database import Base

class Logs(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    date_access: Mapped[date] = mapped_column(nullable=False)
    ip_address: Mapped[str]
    user_agent: Mapped[str]

    #employee: Mapped["Employess"] = relationship("Employees", back_populates="logs")

    class Config:
        from_attributes = True