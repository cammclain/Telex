from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configuration class to hold all environment variables
class Config:
    # C2 Server
    C2_HOST = os.getenv('C2_HOST', 'http://localhost:5000')
    C2_PORT = int(os.getenv('C2_PORT', 5000))
    
    # Telegram Bot
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///c2.db')
