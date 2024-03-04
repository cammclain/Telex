from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters
from ..config import Config
from ..shared.data.database import create_schema
from ..shared.integrations.commands.command_loader import load_and_execute_command  # Adjust the import path as necessary
import logging






## Import commands

from ..shared.integrations.commands.user_commands.standard_comands.start import start
from ..shared.integrations.commands.user_commands.standard_comands.help import help_command


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # This is important to give immediate feedback to the user
    
    if query.data == "help":
        await help_command(update, context)  # Assuming help_command can handle being called like this
    
    elif query.data == "start":
        await start(update, context)

    
    
    
    # Handle other callback queries here, e.g., about, commands, list_agents, etc.
    # You might need to adjust your functions or implement new ones to work with callback queries



async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_name = update.message.text.strip("/")
    try:
        # Example usage, adjust parameters as necessary for your command functions
        result = load_and_execute_command(command_name, agent_id="example_agent_id", additional_data="data")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(result))
    except ValueError as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))

from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters
from ..config import Config
from ..shared.data.database import create_schema
from ..shared.integrations.commands.command_loader import load_and_execute_command  # Adjust the import path as necessary
import logging

from ..user_interface_bot.core import handle_command, callback_query_handler

def interface_manager():
    import datetime

    # Enable logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    logging.getLogger("httpx").setLevel(logging.INFO)  # Set higher logging level for httpx
    logger = logging.getLogger(__name__)

    # Initialize Telegram Bot application
    application = Application.builder().token(Config.USER_INTERFACE_BOT_TOKEN).build()
    
    # Create database schema
    create_schema()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # Register a message handler for text messages to handle commands dynamically
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_command))
    # Inside main()
    application.add_handler(CallbackQueryHandler(callback_query_handler))

    # Start the bot
    application.run_polling()
