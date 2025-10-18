"""Location schemas."""

from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel


class LocationBase(BaseModel):
    """Base location schema."""

    name: str
    description: Optional[str] = None
    city: str
    address: Optional[str] = None
    latitude: float
    longitude: float
    category: str
    subcategories: Optional[List[str]] = None


class LocationCreate(LocationBase):
    """Location creation schema."""

    external_id: Optional[str] = None
    external_source: Optional[str] = None
    rating: Optional[float] = None
    working_hours: Optional[Dict[str, str]] = None
    ticket_info: Optional[Dict[str, any]] = None
    photos: Optional[List[str]] = None
    website: Optional[str] = None
    phone: Optional[str] = None


class LocationUpdate(BaseModel):
    """Location update schema."""

    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    rating: Optional[float] = None
    working_hours: Optional[Dict[str, str]] = None
    ticket_info: Optional[Dict[str, any]] = None
    photos: Optional[List[str]] = None


class LocationInDB(LocationBase):
    """Location in database schema."""

    id: int
    rating: Optional[float] = None
    reviews_count: int
    working_hours: Optional[Dict[str, str]] = None
    ticket_info: Optional[Dict[str, any]] = None
    external_id: Optional[str] = None
    external_source: Optional[str] = None
    photos: Optional[List[str]] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic config."""

        from_attributes = True


class Location(LocationInDB):
    """Location response schema."""

    pass


class LocationSearchRequest(BaseModel):
    """Location search request schema."""

    city: str
    category: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[int] = 5000  # в метрах
    limit: Optional[int] = 20

