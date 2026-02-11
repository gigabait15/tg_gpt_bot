from aiogram import Router, F
from aiogram.types import CallbackQuery

from core.database.db import db_session
from src.keyboards import get_main_keyboard

router = Router()


@router.callback_query(F.data == "new_request")
async def cb_new_request(callback: CallbackQuery):
    await db_session.clear_history(callback.from_user.id)
    await callback.message.edit_text(
        "Контекст сброшен. Отправь новый запрос.",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()
