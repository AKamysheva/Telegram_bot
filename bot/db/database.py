from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from bot.config import settings


engine = create_async_engine(settings.database_url, echo=False)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
