from aiogram.types import InlineQuery,InlineQueryResultArticle,InputTextMessageContent,InlineQueryResultPhoto
from config import dp
from keyboards import pyhton_inline_kb

@dp.inline_handler(text="python")
async def python_query(query:InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultArticle(
        id="1",
        title="Python kurslari",
        input_message_content=(InputTextMessageContent(message_text="Bizning python kurslarimiz haqida")),
        reply_markup=pyhton_inline_kb
        )
        ]
    )


@dp.inline_handler(text="pyphoto")
async def pyphoto_query(query:InlineQuery):
    await query.answer(
        results=[
            InlineQueryResultPhoto(
        id="2",
        title="Python kurslari",
        thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
        photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
        caption="Python kurslari",
        reply_markup=pyhton_inline_kb
        )
        ]
    )


@dp.inline_handler()
async def empty_query(query:InlineQuery):
    await query.answer(
        results=[
        InlineQueryResultArticle(
        id="test1",
        title="Telegram Bot kursi",
        input_message_content=(InputTextMessageContent(message_text="Bizning telegram bot kurslarimiz haqida")),
        url="t.me//coder_ali",
        thumb_url="https://www.addtelegrammember.com/wp-content/webpc-passthru.php?src=https://www.addtelegrammember.com/wp-content/uploads/2020/12/Telegram-Bot-1200x600.jpg&nocache=1",
        description="Kurs haqida"
    ),
    # InlineQueryResultArticle(
        
    # )
    ]
    )