"""Location model."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, JSON, String, Text

from app.db.base import Base


class Location(Base):
    """Location model - туристическая локация."""

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    
    # Основная информация
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    city = Column(String, nullable=False, index=True)
    address = Column(String, nullable=True)
    
    # Координаты
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    # Категории
    category = Column(String, nullable=False, index=True)  # museum, park, restaurant, etc.
    subcategories = Column(JSON, nullable=True)  # ["art_museum", "modern_art"]
    
    # Рейтинг и популярность
    rating = Column(Float, nullable=True)
    reviews_count = Column(Integer, default=0)
    
    # Время работы и билеты
    working_hours = Column(JSON, nullable=True)  # {"mon": "9:00-18:00", ...}
    ticket_info = Column(JSON, nullable=True)  # {"price": 500, "booking_url": "..."}
    
    # Внешние ID
    external_id = Column(String, nullable=True, index=True)  # ID в OpenTripMap или Yandex
    external_source = Column(String, nullable=True)  # "opentripmap" или "yandex"
    
    # Метаданные
    photos = Column(JSON, nullable=True)  # URLs фотографий
    website = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

