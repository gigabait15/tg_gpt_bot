from aiogram import Router, F
from aiogram.types import Message
import logging
from core.database.db import db_session
from src.gpt import get_chat_response
from src.keyboards import get_main_keyboard

router = Router()


@router.message(F.text)
async def handle_text(message: Message):
    text = message.text.strip()
    if not text:
        return

    status_msg = await message.answer("Думаю...")

    try:
        history = await db_session.get_history(message.from_user.id)
        response = get_chat_response(history, text)

        await db_session.add_message(message.from_user.id, "user", text)
        await db_session.add_message(message.from_user.id, "model", response)

        await status_msg.edit_text(response, reply_markup=get_main_keyboard())
    except Exception as e:
        logging.error(f"Error: {e}")
        await status_msg.edit_text("Произошла ошибка при генерации ответа. Попробуйте позже.", reply_markup=get_main_keyboard())
