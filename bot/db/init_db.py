import asyncio
from sqlalchemy import text
from bot.db.database import async_session


async def init_db():
    with open("bot/db/init.sql", "r", encoding="utf-8") as file:
        sql = file.read()
    async with async_session() as session:
        async with session.begin():
            statements = [s.strip() for s in sql.split(";") if s.strip()]
            for stmt in statements:
                await session.execute(text(stmt))


if __name__ == "__main__":
    asyncio.run(init_db())
