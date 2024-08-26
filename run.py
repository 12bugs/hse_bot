import asyncio
import logging 

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from config import TOKEN
from app.handlers import router as user_router
from app.admin import admin as admin_router
from app.database.models import async_main


async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
