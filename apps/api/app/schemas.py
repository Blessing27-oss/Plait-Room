# Pydantic schemas define what data the API accepts and returns.
from datetime import date, time, datetime
from pydantic import BaseModel, ConfigDict


class AvailabilityCreate(BaseModel):
    date: date
    start_time: time


class AvailabilityResponse(AvailabilityCreate):
    id: int
    is_available: bool
    created_at: datetime | None

    model_config = ConfigDict(from_attributes=True)