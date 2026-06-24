from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/text2sql"

engine = create_engine(
    DATABASE_URL,
    echo=True
)