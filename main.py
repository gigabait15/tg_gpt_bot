import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web
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


async def handle(request):
    return web.Response(text="I am alive")

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port=8080)
    await site.start()

asyncio.create_task(run_web_server())
if __name__ == "__main__":
    asyncio.run(main())
