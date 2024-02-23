from ...core.config import Config

BOT_NAME = Config.BOT_NAME
BOT_TAG = Config.BOT_TAG

### General Strings
WELCOME_MESSAGE = f"Welcome to {BOT_NAME}, your reliable Command and Control (C2) assistant."
ABOUT_MESSAGE = f"{BOT_NAME} ({BOT_TAG}) is designed to facilitate remote management and operations of networked agents. It provides a secure and intuitive interface for conducting reconnaissance, executing commands, and managing assets."

### Error Messages
ERROR_INVALID_COMMAND = "Oops! That seems like an invalid command. Please try again or use /help to see available commands."
ERROR_AGENT_NOT_FOUND = "The specified agent could not be found. Please check the agent ID and try again."
ERROR_NO_ACTIVE_AGENTS = "Currently, there are no active agents. Ensure your agents are correctly configured and online."

### User Interface Strings
START_MESSAGE = f"{WELCOME_MESSAGE}\n\nType /help for a list of available commands."
HELP_MESSAGE = f"{BOT_NAME} C2 can assist you with the following commands:\n\n" \
               "STANDARD COMMANDS:\n" \
               "/start - Start interaction with the C2 bot.\n" \
               "/help - Get detailed help and a list of commands.\n\n" \
               "AGENT COMMANDS:\n" \
               "/checkin - Trigger an agent check-in.\n" \
               "/execute - Execute a command on a target system.\n" \
               "/exfiltrate - Initiate data exfiltration from a target.\n" \
               "/list_agents - List all registered and active agents.\n" \
               "/agent_info - Get detailed information about a specific agent.\n\n" \
               "MANAGEMENT COMMANDS:\n" \
               "/add_user - Add a new user to the C2 system (Admin only).\n" \
               "/remove_user - Remove a user from the C2 system (Admin only)."

### Agent Interaction Strings
AGENT_CHECKIN_SUCCESS = "Agent check-in successful. The system is now ready to receive commands."
AGENT_EXECUTE_COMMAND = "Please enter the command to execute on the target system:"
AGENT_DATA_EXFILTRATION = "Please specify the file path for exfiltration:"

### Management Commands Strings
ADD_USER_PROMPT = "Please enter the username for the new user:"
REMOVE_USER_PROMPT = "Please enter the username of the user to remove:"

### Success and Confirmation Messages
SUCCESS_AGENT_COMMAND_EXECUTED = "The command has been successfully executed on the target system."
SUCCESS_DATA_EXFILTRATED = "Data has been successfully exfiltrated and is now available for review."
SUCCESS_USER_ADDED = "The new user has been successfully added to the C2 system."
SUCCESS_USER_REMOVED = "The user has been successfully removed from the C2 system."

### Inline Keyboard Strings
INLINE_KEYBOARD_ABOUT = "Learn more about what this bot can do."
INLINE_KEYBOARD_HELP = "Get a list of commands and how to use them."
INLINE_KEYBOARD_COMMANDS = "View and execute available commands."
INLINE_KEYBOARD_LIST_AGENTS = "List and manage active agents."
INLINE_KEYBOARD_EXECUTE = "Execute a command on an agent."
INLINE_KEYBOARD_EXFILTRATE = "Initiate data exfiltration from an agent."
