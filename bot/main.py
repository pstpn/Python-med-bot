from utils.excel import save_excel_to_db
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.handlers import router, stop_handle
from loguru import logger
from asyncio import run
from os import getenv
from sqlalchemy import create_engine


# The main asynchronous function for the application
async def main():
    # Configure the logger
    logger.add(
        "logs/debug.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="30 KB",
        compression="zip",
    )

    # Save input data from Excel to database
    logger.info("parse excel to database")
    save_excel_to_db(create_engine(getenv("DATABASE_URL"), pool_recycle=1800))

    # Create a Bot instance
    bot = Bot(token=getenv("BOT_TOKEN"), parse_mode='markdown')

    # Create a Dispatcher instance with in-memory storage and include the defined router
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    # Start polling
    logger.info("start bot")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    # Stop bot and close database connection
    logger.info("stop bot and close database connection")
    await stop_handle()


if __name__ == "__main__":
    run(main())
