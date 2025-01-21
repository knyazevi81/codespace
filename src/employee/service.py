from sqlalchemy import insert, select, and_, or_

from src.service.base import BaseService
from src.employee.models import Employess
from src.database import async_session_maker


class EployService(BaseService):
    model=Employess

    @classmethod
    async def add(cls):
        async with async_session_maker() as session:
            ...