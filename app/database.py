import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./finanzas.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
