from telegram import Update
from telegram.ext import ContextTypes
from ....user_interface.strings import ABOUT_MESSAGE

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=ABOUT_MESSAGE)
