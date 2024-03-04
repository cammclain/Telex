from telegram import Update
from telegram.ext import ContextTypes
from ....user_interface.strings import START_MESSAGE
from ....user_interface.inline_keyboards import start_inline_markup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=START_MESSAGE, 
        reply_markup=start_inline_markup
    )
