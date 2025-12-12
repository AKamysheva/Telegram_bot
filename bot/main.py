import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import text
from bot.config import settings
from bot.service import generate_sql
from bot.db.database import async_session

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer("Привет! Я бот для аналитики видео! Задай свой вопрос.")


@dp.message()
async def handle_message(message: Message) -> None:
    user_question = message.text
    sql_query = await generate_sql(user_question)
    if sql_query.startswith("Некорректный"):
        await message.answer("Некорректный вопрос.")
        return

    async with async_session() as session:
        result = await session.execute(text(sql_query))
        value = result.scalar()

    await message.answer(str(value))


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
