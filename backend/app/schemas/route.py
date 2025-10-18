"""Route schemas."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class LocationInRoute(BaseModel):
    """Location in route schema."""

    id: int
    location_id: int
    order: int
    visit_time: Optional[datetime] = None
    duration: Optional[int] = None
    notes: Optional[str] = None
    is_visited: bool = False

    class Config:
        """Pydantic config."""

        from_attributes = True


class RouteBase(BaseModel):
    """Base route schema."""

    title: str
    description: Optional[str] = None
    city: str
    start_date: datetime
    end_date: datetime
    interests: Optional[List[str]] = None


class RouteCreate(RouteBase):
    """Route creation schema."""

    pass


class RouteUpdate(BaseModel):
    """Route update schema."""

    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    interests: Optional[List[str]] = None
    is_public: Optional[bool] = None


class RouteInDB(RouteBase):
    """Route in database schema."""

    id: int
    user_id: int
    is_completed: bool
    is_public: bool
    total_duration: Optional[int] = None
    total_distance: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic config."""

        from_attributes = True


class Route(RouteInDB):
    """Route response schema."""

    locations: List[LocationInRoute] = []


class RouteGenerateRequest(BaseModel):
    """Request schema for AI route generation."""

    city: str
    start_date: datetime
    end_date: datetime
    interests: List[str]
    max_locations_per_day: Optional[int] = 5
    preferred_start_time: Optional[str] = "09:00"
    preferred_transport: Optional[str] = "walking"  # walking, public_transport, car

