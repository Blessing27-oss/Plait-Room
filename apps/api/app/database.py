"""database connections/sessions"""

import os

from dotenv import load_dotenv
# SqlAlchemy describes and interacts with the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# Alembic tracks changes to the structure of that database.


# loads variables from .env
load_dotenv()

# retrieves our connections string
DATABASE_URL = os.getenv("DATABASE_URL")

# creates SQLAlchemy's central connection interface to PostgreSQL
engine = create_engine(DATABASE_URL)

# SessionLocal will let individual API requests open a database session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
class Base(DeclarativeBase):
    pass

# introduces a database session. My engine represents the application's connection infrastructure to PostgreSQL. 
# But when an individual API request needs to do database work, SQLAlchemy uses a Session.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

