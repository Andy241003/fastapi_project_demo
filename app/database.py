from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  # Đảm bảo nó nạp file .env

MYSQL_URL = os.getenv("MYSQL_URL")

engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
