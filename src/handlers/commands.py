from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from core.database.db import db_session
from src.keyboards import get_main_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await db_session.clear_history(message.from_user.id)
    await message.answer(
        "Привет! Отправь любое сообщение — я отвечу через ChatGPT. "
        "История диалога сохраняется. Нажми «Новый запрос», чтобы начать с нуля.",
        reply_markup=get_main_keyboard()
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — сбросить контекст и начать заново\n"
        "/help — эта справка\n\n"
        "Отправь текст — получишь ответ от ChatGPT. "
        "Бот учитывает предыдущие сообщения в диалоге.",
        reply_markup=get_main_keyboard()
    )
