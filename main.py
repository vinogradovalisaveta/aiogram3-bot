import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from app.user import router
from database.models import async_main

# загрузка переменных окружения из .env
load_dotenv()

# инициализация бота с токеном и включением html-форматирования
bot = Bot(token=os.getenv("TOKEN"), DefaultBotProperties=ParseMode.HTML)
# инициализация диспетчера для обработки событий
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router)
    # очистка очереди ожидающих сообщений (пока бот был off)
    await bot.delete_webhook(drop_pending_updates=True)
    # запуск бота для обработки событий
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
