import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://<YOUR_GH_PAGES>/")

if not TOKEN:
    raise RuntimeError("Please set BOT_TOKEN in environment")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("✨ Мои итоги", web_app=WebAppInfo(url=WEBAPP_URL)))
    await message.answer("Привет! Нажми кнопку, чтобы открыть Итоги года.", reply_markup=kb)

@dp.message_handler(commands=['stats'])
async def stats_cmd(message: types.Message):
    await message.answer("Открой мини‑приложение, чтобы посмотреть персональные итоги.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
