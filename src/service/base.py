from sqlalchemy import select, insert
from typing import TypeVar, Generic, Type

from src.database import async_session_maker

T = TypeVar("T")

class BaseService(Generic[T]):
    model: Type[T] = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(
                    **kwargs
                )
            )
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(
                    **kwargs
                )
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_id(cls, model_id):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(
                    id=model_id
                )
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(
                    **data
                )
            )
            await session.execute(query)
            await session.commit()
