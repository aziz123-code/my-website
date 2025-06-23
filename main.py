import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums.chat_type import ChatType

from yandex import yandex_spell_check
from db import BOT_TOKEN, save_request
from validators import has_negative_words, find_tags
from validators import is_valid_request, looks_like_request




bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



@dp.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def check_message(message: types.Message):
    user_text = message.text or message.caption
    if not user_text:
        return

    user_text = user_text.strip()
    corrected_text = yandex_spell_check(user_text)
    corrected_text = ' '.join(corrected_text.split())

    if has_negative_words(corrected_text):
        await message.reply("\U0001F6AB В вашей заявке обнаружена недопустимая формулировка. Пожалуйста, "
                                "переформулируйте.")
        return

    if is_valid_request(corrected_text):
        tags = find_tags(corrected_text)
        tags_result = "/".join(tags) if tags else "без тегов"
        save_request(tags_result, corrected_text)
        await message.reply(f"\u2705 Ваша заявка принята и отправлена на обработку.")

        return


    if looks_like_request(corrected_text):
        await message.reply("\u26A0 Заявка заполнена неправильно. Пожалуйста следуйте регламенту.")
        return

    return


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
