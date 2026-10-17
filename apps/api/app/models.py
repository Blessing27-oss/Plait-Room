"""PostgreSQL table definitions"""

from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

# our model inherits from base
# SQLAlchemy collects information about tables belonging to Base inside Base.metadata. So Alembic can now inspect
from app.database import Base
from sqlalchemy import (
    Column, Integer, Date, Time,
    Boolean, DateTime, UniqueConstraint
)
from datetime import datetime, timezone
# This is our ORM model, each python attribute matches to a PostgreSQL column
class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True)

    date = Column(Date, nullable=False)

    start_time = Column(Time, nullable=False)

    is_available = Column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        UniqueConstraint("date", name="uq_availability_date"),
    )

