import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.settings import settings
from core.database.db import db_session
from src.handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN_TG, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(router)


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await db_session.close()


if __name__ == "__main__":
    asyncio.run(main())
