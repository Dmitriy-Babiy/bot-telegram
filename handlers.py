from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("@router.message(Command(start))")


@router.message()
async def message_handler(msg: Message):
    await msg.reply("Неизвестная команда")

@router.message(Command("buttons"))
async def buttons_handler(msg: Message):
    await msg.answer("@router.message(Command(buttons))")
