"""Gamification service for achievements and points."""

from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.achievement import Achievement, UserAchievement
from app.models.user import User


class GamificationService:
    """Service for gamification features."""

    async def check_achievements(
        self,
        user_id: int,
        action: str,
        db: Session,
    ) -> List[Achievement]:
        """
        Check and unlock achievements after user action.
        
        Args:
            user_id: User ID
            action: Action type (route_completed, city_visited, etc.)
            db: Database session
            
        Returns:
            List of newly unlocked achievements
        """
        unlocked = []
        
        # TODO: Implement achievement checking logic
        # Actions could be:
        # - route_completed
        # - city_visited
        # - location_visited
        # - route_shared
        # - days_streak
        
        return unlocked

    async def award_points(
        self,
        user_id: int,
        points: int,
        reason: str,
        db: Session,
    ) -> int:
        """
        Award points to user.
        
        Args:
            user_id: User ID
            points: Points to award
            reason: Reason for points
            db: Database session
            
        Returns:
            New total points
        """
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.points += points
            db.commit()
            return user.points
        
        return 0

    async def get_leaderboard(
        self,
        limit: int = 10,
        city: Optional[str] = None,
        db: Session = None,
    ) -> List[dict]:
        """
        Get leaderboard of top users.
        
        Args:
            limit: Number of users
            city: Filter by city
            db: Database session
            
        Returns:
            Leaderboard data
        """
        # TODO: Implement leaderboard query
        # Consider:
        # - Total points
        # - Monthly points
        # - City-specific leaderboard
        
        leaderboard = []
        return leaderboard

    async def get_user_achievements(
        self,
        user_id: int,
        db: Session,
    ) -> List[UserAchievement]:
        """
        Get user's achievements with progress.
        
        Args:
            user_id: User ID
            db: Database session
            
        Returns:
            List of user achievements
        """
        achievements = (
            db.query(UserAchievement)
            .filter(UserAchievement.user_id == user_id)
            .all()
        )
        
        return achievements

    def _create_default_achievements(self, db: Session):
        """Create default achievements."""
        default_achievements = [
            {
                "code": "first_route",
                "name": "Первый маршрут",
                "description": "Создайте свой первый маршрут",
                "points": 10,
                "condition_type": "routes_created",
                "condition_value": 1,
            },
            {
                "code": "explorer",
                "name": "Исследователь",
                "description": "Посетите 10 локаций",
                "points": 50,
                "condition_type": "locations_visited",
                "condition_value": 10,
            },
            {
                "code": "city_master",
                "name": "Знаток города",
                "description": "Посетите 5 городов",
                "points": 100,
                "condition_type": "cities_visited",
                "condition_value": 5,
            },
            {
                "code": "social_butterfly",
                "name": "Социальная бабочка",
                "description": "Поделитесь 5 маршрутами",
                "points": 30,
                "condition_type": "routes_shared",
                "condition_value": 5,
            },
        ]
        
        for ach_data in default_achievements:
            existing = db.query(Achievement).filter(
                Achievement.code == ach_data["code"]
            ).first()
            
            if not existing:
                achievement = Achievement(**ach_data)
                db.add(achievement)
        
        db.commit()

