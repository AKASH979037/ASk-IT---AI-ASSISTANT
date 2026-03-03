import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the application"""
    API_KEY = os.getenv('API_KEY')
    DEBUG = os.getenv('DEBUG', True)
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @staticmethod
    def init_app(app):
        """Initialize app with configuration"""
        pass
