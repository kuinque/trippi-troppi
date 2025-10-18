"""Route model."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class Route(Base):
    """Route model - туристический маршрут."""

    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    city = Column(String, nullable=False)
    
    # Даты путешествия
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    
    # Статус
    is_completed = Column(Boolean, default=False)
    is_public = Column(Boolean, default=False)
    
    # Метаданные
    total_duration = Column(Integer, nullable=True)  # в минутах
    total_distance = Column(Float, nullable=True)  # в километрах
    
    # Интересы (категории)
    interests = Column(JSON, nullable=True)  # ["museums", "parks", "food"]
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="routes")
    locations = relationship("RouteLocation", back_populates="route", cascade="all, delete-orphan", order_by="RouteLocation.order")


class RouteLocation(Base):
    """RouteLocation - связь между маршрутом и локацией."""

    __tablename__ = "route_locations"

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    
    # Порядок в маршруте
    order = Column(Integer, nullable=False)
    
    # Время посещения
    visit_time = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)  # Планируемое время на месте (минуты)
    
    # Заметки пользователя
    notes = Column(Text, nullable=True)
    
    # Статус
    is_visited = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    route = relationship("Route", back_populates="locations")
    location = relationship("Location")

