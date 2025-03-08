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

# Обработчик Inline-запросов
@dp.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery):
    query = inline_query.query  # Запрос, который пользователь вводит после @botname

    # Если запрос пустой, не показываем результаты
    if not query:
        return

    # Формируем результаты запроса
    results = [
        InlineQueryResultArticle(
            id=random.randint(1, 1000000),  # Уникальный ID для каждого результата
            title="Кто ты из MR PENIS CHAT?",  # Название подсказки
            input_message_content=InputTextMessageContent(random.choice(random_messages))  # Содержимое сообщения
        )
    ]

    # Отправляем результаты запроса (показ подсказок)
    await bot.answer_inline_query(inline_query.id, results)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())