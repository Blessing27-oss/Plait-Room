"""PostgreSQL table definitions"""


from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

# our model inherits from base
# SQLAlchemy collects information about tables belonging to Base inside Base.metadata. So Alembic can now inspect
from app.database import Base

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