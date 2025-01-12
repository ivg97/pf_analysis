from core.config import app_settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


engine = create_async_engine(app_settings.db_url, future=True)
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

