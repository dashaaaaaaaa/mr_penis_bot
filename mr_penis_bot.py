import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated
from aiogram.enums import ChatType

TOKEN = "7720767705:AAGCz87dzusbLM1zrKMLh04jvnfHSwnloKE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список рандомных сообщений
random_messages = [
    "Ты – Катя Пряхина! Ты хочешь отсосать на профсе",
    "Ты — Анатолий Ларкин! Ты хочешь ебаться с Тимуром в громакс",
    "Ты — Тимур Кулагин! Ты хочешь ебаться с Анатолием в громакс",
    "Ты — Александр Милек! Ты хочешь ебаться с Анатолием и Тимуром в громакс, но тебя не берут",
    "Ты — Игорь Шарпилов! Игорь иди нахуй",
    "Ты — Екатерина Столбова! КАК ЖЕ МНЕ ПОХУЙ ZZZZ VVVVVVV",
    "Ты — еЛЕНА кУДРЯВЦЕВА! Тебя ебет сберкот",
    "Ты — Всеволод Ершов! ТОЛСТЫЙ ЖИРНЫЙ ЧЛЕН",
    "Ты — Петр Фомин! И его большой орган",
    "Ты — Амина Имарналсшалиева! Самый милый член сообщества",
    "Ты — Екатерина Глупышкина! Или штанишкина или свошкина",
    "Ты — Соня Сырцева! У тебя big dick energy",
    "Ты — СОНИК! Ты из сыктывкатврытра",
    "Ты — Дарья Ольховик! ГЛАВНЫЙ ЧЛЕН ГОЙДААААААА БАЗА"
]

# Фильтр сообщений, если тегнули бота
@dp.message()
async def mention_response(message: types.Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        if message.text and (message.bot or f"@{(await bot.me()).username}" in message.text):
            await message.reply(random.choice(random_messages))

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
