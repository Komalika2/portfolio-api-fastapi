# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: DB URL and engine setup
DATABASE_URL = "sqlite:///./portfolio.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Step 2: DB session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Step 3: Base class for models
Base = declarative_base()

# Step 4: Import models so metadata knows about tables
from app import models

# Step 5: Create tables
Base.metadata.create_all(bind=engine)
