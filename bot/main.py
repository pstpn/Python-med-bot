from utils.excel import save_excel_to_db
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.handlers import router, stop_handle
from loguru import logger
from asyncio import run
from os import getenv
from sqlalchemy import create_engine


async def main():
    logger.add(
        "logs/debug.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="30 KB",
        compression="zip",
    )

    logger.info("parse excel to database")
    save_excel_to_db(create_engine(getenv("DATABASE_URL"), pool_recycle=1800))

    bot = Bot(token=getenv("BOT_TOKEN"), parse_mode="html")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    logger.info("start bot")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    logger.info("stop bot and close database connection")
    await stop_handle()


if __name__ == "__main__":
    run(main())
