from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///code_space.db")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


#async def delete_tables():
#    async with engine.begin() as conn:
#        await conn.run_sync(Base.metadata.drop_all)


class Base(DeclarativeBase):
    pass

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
