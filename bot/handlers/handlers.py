from messages import messages
from database.database import Database
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from asyncio import get_event_loop
from os import getenv
from utils.excel import save_report_to_excel


router = Router()
db = Database(getenv("DATABASE_URL"), loop=get_event_loop())


@router.message(Command("start"))
async def start_handler(msg: Message):
    """welcome message"""

    await msg.answer(messages["welcome"])


@router.message(Command("help"))
async def help_handler(msg: Message):
    """help info"""

    await msg.answer(messages["help"])


@router.message(Command("contacts"))
async def contacts_handler(msg: Message) -> None:
    """contacts"""

    await msg.answer(messages["contacts"])


@router.message(Command("contacts"))
async def contacts_handler(msg: Message) -> None:
    """contacts"""

    await msg.answer(messages["contacts"])


@router.message(Command("report"))
async def report_handler(msg: Message) -> None:
    """get report"""

    report = await db.get_report()
    save_report_to_excel(report)

    await msg.reply_document(
        document="data/new_report.xlsx",
        filename="report.xlsx",
        caption=messages["report"],
    )


@router.message()
async def unknown_handler(msg: Message) -> None:
    """handler for unknown messages"""

    if not msg.is_command():
        await msg.answer(messages["format_error"])
    else:
        await msg.answer(messages["command_error"])


async def stop_handle():
    """stop handle"""

    await db.close_database()
