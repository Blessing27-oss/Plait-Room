"""database connections/sessions"""

# SqlAlchemy describes and interacts with the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# Alembic tracks changes to the structure of that database.

# retrieves our connections string (config.py checks it exists)
from app.config import DATABASE_URL

# creates SQLAlchemy's central connection interface to PostgreSQL.
# pool_pre_ping checks a connection still works before using it. Neon closes connections
# when the database sleeps after inactivity, so without this the first request after a pause could fail.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

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

