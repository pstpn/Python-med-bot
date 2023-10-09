from messages import messages
from database.database import Database
from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from asyncio import get_event_loop
from os import getenv
from utils.excel import save_report_to_excel, output_filename


# Create an instance of the Router class
router = Router()

# Create an instance of the Database class, using a database URL from environment variables
db = Database(getenv("DATABASE_URL"), loop=get_event_loop())


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    """
    Message handler for the `/start` command
    """
    await msg.answer(messages["start"])


@router.message(Command("help"))
async def help_handler(msg: Message) -> None:
    """
    Message handler for the `/help` command
    """
    await msg.answer(messages["help"])


@router.message(Command("contacts"))
async def contacts_handler(msg: Message) -> None:
    """
    Message handler for the `/contacts` command
    """
    await msg.answer(messages["contacts"])


@router.message(Command("report"))
async def report_handler(msg: Message) -> None:
    """
    Message handler for the `/report` command
    """
    # Retrieve a report from the database
    report = await db.get_report()

    # Save the report to an Excel file
    save_report_to_excel(report)

    # Reply to the user with the Excel document containing the report
    await msg.reply_document(
        document=FSInputFile(output_filename), caption=messages["report"]
    )


async def stop_handle() -> None:
    """
    Stop handle
    """
    # Close the database connection
    await db.close_database()
