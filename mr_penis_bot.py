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
    "Ты – Катя Пряхина! Тебя хотят выебать 40 человек!", 
    "Ты – Князев! Жаль, что далеко не все поймут в чем же дело)))) действительно тонко)))) не так уж много образованных в наше время, кто знает, почему это так интересно и необычно",
    "Ты — Анатолий Ларкин! СОСИ ЯЙЦА",
    "Ты — Анатолий Ларкин! шило мыло хуй анатолий ларкин",
    "Ты — Тимур Кулагин! Ты хочешь ебаться с Анатолием в громакс",
    "Ты — Тимур Кулагин! ебись в яйца",
    "Ты — Александр Милек! Ты хочешь ебаться с Анатолием и Тимуром в громакс, но тебя не берут",
    "Ты — Игорь Шарпилов! Игорь иди нахуй",
    "Ты — Екатерина Столбова! КАК ЖЕ МНЕ ПОХУЙ ZZZZ VVVVVVV",
    "Ты — еЛЕНА кУДРЯВЦЕВА! Тебя ебет сберкот",
    "Ты — Всеволод Ершов! ОГРОМНЫЙ ЧЕРНЫЙ ЧЛЕН",
    "Ты — Всеволод Ершов! Никому не рассказывай, что ты сладко делал сегодня утром"
    "Ты — Петр Фомин! И его большой орган",
    "Ты — Амина Имарналсшалиева! Самый милый член сообщества",
    "Ты — Екатерина Глупышкина! Или штанишкина или свошкина",
    "Ты — Соня Сырцева! У тебя big dick energy",
    "Ты — СОНИК! Ты из сыктывкатврытра",
    "Ты — Дарья Ольховик! ГЛАВНЫЙ ЧЛЕН ГОЙДААААААА БАЗА"
]

wish_messages = [
    "Пожелание от Никулина! Береги свои органоиды",
    "Пожелание от Слободова! жесть",
    "Пожелание от Германа! НЕ СУЙТЕ ОГРОМНЫЙ ЧЕРНЫЙ ЧЛЕН МНЕ В ЖОПУ",
    "Пожелание от Тоника! ГДЕ МОИ ДЕНЬГИ УЕБОК",
    "Пожелание от шКУРНИКОВА! тимур возьми пробу говна у одноклассников",
    "Пожелание от Степановой! даваааай да давай ешь чипсы дааааа ешь чипсы дАВААЙ",
]

@dp.inline_query()
async def inline_query_handler(inline_query: types.InlineQuery):
    query = inline_query.query  # Запрос пользователя после @botname

    results = [
        InlineQueryResultArticle(
            id=str(random.randint(1, 1000000)),
            title="Кто ты из MR PENIS CHAT?",  # Первая рубрика
            input_message_content=InputTextMessageContent(message_text=random.choice(random_messages))
        ),
        InlineQueryResultArticle(
            id=str(random.randint(1, 1000000)),
            title="Пожелание от преподов ФББНИУВШЭ",  # Вторая рубрика
            input_message_content=InputTextMessageContent(message_text=random.choice(wish_messages))
        )
    ]

    await bot.answer_inline_query(inline_query.id, results, cache_time=0)


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
