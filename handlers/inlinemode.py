from aiogram.types import InlineQuery,InlineQueryResultArticle,InputTextMessageContent
from config import dp

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