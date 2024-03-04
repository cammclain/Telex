from telegram import Update
from telegram.ext import ContextTypes
from ....user_interface.strings import HELP_MESSAGE

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Determine if this was called from a command or a callback query
    chat_id = update.effective_chat.id if update.effective_chat else update.callback_query.message.chat.id
    
    await context.bot.send_message(chat_id=chat_id, text=HELP_MESSAGE)
