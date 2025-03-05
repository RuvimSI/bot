import logging
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "7612631102:AAFPt7du69ljHoiXrote3H8UwM-QjQJ0hYU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

GROUPS = {
    "Музей шоколада": "https://t.me/+00B3_VQJLJA4NmVi",
    "Музей мороженного": "https://t.me/+SsJvQDluIro4NjMy",
    "Музей карамели": "https://t.me/+jlDp9vsUrOJkNTgy",
    "Боулинг ТЦ Глобус": "https://t.me/+rU2GSPRs4JxmYjI6",
    "WarPoint ТЦ Алые паруса": "https://t.me/+jgnB1wen-2dlZTdi"
}

user_choices = {}

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_button = KeyboardButton(
        text="Выбрать мероприятие",
        web_app=WebAppInfo(url="https://telegram-webapp.onrender.com")
    )
    keyboard.add(web_app_button)

    await message.answer("Нажмите кнопку ниже, чтобы выбрать мероприятие:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_callback(message: types.Message):
    choice = message.web_app_data.data
    user_choices[message.from_user.id] = choice
    link = GROUPS.get(choice, "#")
    
    await message.answer(f"Вы выбрали: {choice}\nСсылка на беседу: {link}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)