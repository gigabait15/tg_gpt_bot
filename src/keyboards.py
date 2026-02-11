from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

NEW_REQUEST_BTN = InlineKeyboardButton(
    text="Новый запрос",
    callback_data="new_request"
)

def get_main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[NEW_REQUEST_BTN]])
