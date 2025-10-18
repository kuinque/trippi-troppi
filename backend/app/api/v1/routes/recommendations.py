"""Recommendation routes."""

from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.routes.auth import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.services.recommendations import RecommendationService

router = APIRouter()


@router.get("/")
async def get_recommendations(
    city: str = None,
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Get personalized recommendations for current user."""
    service = RecommendationService()
    
    recommendations = await service.get_personalized_recommendations(
        user_id=current_user.id,
        city=city,
        limit=limit,
        db=db,
    )
    
    return {
        "recommendations": recommendations,
        "total": len(recommendations),
    }


@router.get("/routes/trending")
async def get_trending_routes(
    city: str = None,
    limit: int = 10,
    db: Session = Depends(get_db),
) -> Any:
    """Get trending routes."""
    service = RecommendationService()
    
    trending = await service.get_trending_routes(
        city=city,
        limit=limit,
        db=db,
    )
    
    return {
        "trending": trending,
        "total": len(trending),
    }


@router.get("/routes/{route_id}/similar")
async def get_similar_routes(
    route_id: int,
    limit: int = 5,
    db: Session = Depends(get_db),
) -> Any:
    """Get similar routes."""
    service = RecommendationService()
    
    similar = await service.get_similar_routes(
        route_id=route_id,
        limit=limit,
        db=db,
    )
    
    return {
        "similar_routes": similar,
        "total": len(similar),
    }

