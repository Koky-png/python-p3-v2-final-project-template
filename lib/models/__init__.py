from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL
DATABASE_URL = "sqlite:///carbon_tracker.db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session factory
Session = sessionmaker(bind=engine)

# Base class for ORM models (no need to import models here)
Base = declarative_base()

# Optional: Initialize the database (you can call this from elsewhere)
def initialize_db():
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")
