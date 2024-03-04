import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Initialize a dictionary to hold the configuration of listener bots
listener_bots_config = {
    "listener_bots": [
        {"token": os.getenv("LISTENER_BOT_TOKEN_1")},
        {"token": os.getenv("LISTENER_BOT_TOKEN_2")},
        {"token": os.getenv("LISTENER_BOT_TOKEN_3")},
        {"token": os.getenv("LISTENER_BOT_TOKEN_4")},
        {"token": os.getenv("LISTENER_BOT_TOKEN_5")},
        #{"token": os.getenv("LISTENER_BOT_TOKEN_6")},
        #{"token": os.getenv("LISTENER_BOT_TOKEN_7")},
        #{"token": os.getenv("LISTENER_BOT_TOKEN_8")},
        #{"token": os.getenv("LISTENER_BOT_TOKEN_9")},
        #{"token": os.getenv("LISTENER_BOT_TOKEN_10")}
    ]
}
