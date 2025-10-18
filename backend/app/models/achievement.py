"""Achievement models for gamification."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from app.db.base import Base
from sqlalchemy.orm import relationship


class Achievement(Base):
    """Achievement model - ачивка."""

    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    
    code = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    
    # Иконка и награда
    icon = Column(String, nullable=True)
    points = Column(Integer, default=0)
    
    # Условие получения
    condition_type = Column(String, nullable=False)  # "routes_completed", "cities_visited", etc.
    condition_value = Column(Integer, nullable=False)  # Количество для выполнения
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)


class UserAchievement(Base):
    """UserAchievement - связь пользователя и ачивки."""

    __tablename__ = "user_achievements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    achievement_id = Column(Integer, ForeignKey("achievements.id"), nullable=False)
    
    # Статус
    is_unlocked = Column(Boolean, default=False)
    unlocked_at = Column(DateTime, nullable=True)
    
    # Progress
    progress = Column(Integer, default=0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="achievements")
    achievement = relationship("Achievement")

