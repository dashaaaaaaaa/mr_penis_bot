import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated
from aiogram.enums import ChatType

TOKEN = "7720767705:AAGCz87dzusbLM1zrKMLh04jvnfHSwnloKE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список рандомных сообщений
random_messages = [
    "Ты – Катя Пряхина! Ты хочешь отсосать на профсе",
    "Ты – Князев! Жаль, что далеко не все поймут в чем же дело)))) действительно тонко)))) не так уж много образованных в наше время, кто знает, почему это так интересно и необычно",
    "Ты — Анатолий Ларкин! СОСИ ЯЙЦА",
    "Ты — Анатолий Ларкин! шило мыло хуй анатолий ларкин",
    "Ты — Тимур Кулагин! Ты хочешь ебаться с Анатолием в громакс",
    "Ты — Тимур Кулагин! ебись в яйца",
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

@dp.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery):
    query = inline_query.query  # Запрос, который пользователь вводит после @botname

    # Не проверяем на пустой запрос — всегда возвращаем результаты
    results = [
        InlineQueryResultArticle(
            id=str(random.randint(1, 1000000)),  # Приводим id к строке
            title="Кто ты из MR PENIS CHAT?",      # Название подсказки
            input_message_content=InputTextMessageContent(message_text=random.choice(random_messages))
        )
    ]

    # Отправляем результаты запроса (показ подсказок)
    await bot.answer_inline_query(inline_query.id, results, cache_time=0)


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
