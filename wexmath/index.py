import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import database
import messages

from handlers import router

def quit():
    sys.exit()

def get_token(fileNamePath):
    try:
        return open(fileNamePath, 'r').read()
    except OSError:
        messages.log_error(messages.errorWhileOpeningFile + fileNamePath)
        quit()

async def main():
    token = get_token("token.txt")
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    database.create()
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot, allowed_updates = dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())