from aiogram import Router
from .commands import router as commands_router
from .messages import router as messages_router
from .callbacks import router as callbacks_router

router = Router()
router.include_router(commands_router)
router.include_router(callbacks_router)
router.include_router(messages_router)
