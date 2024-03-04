from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import the Base from the shared base.py
from .base import Base
from ...config import Config

engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)


def create_schema():
    # Create all tables in the database
    Base.metadata.create_all(engine)