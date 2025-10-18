"""Route (travel routes) endpoints."""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.routes.auth import get_current_user
from app.db.session import get_db
from app.models.route import Route
from app.models.user import User
from app.schemas.route import (
    Route as RouteSchema,
    RouteCreate,
    RouteGenerateRequest,
    RouteUpdate,
)
from app.services.ai_agent import AIRouteAgent

router = APIRouter()


@router.post("/generate", response_model=RouteSchema, status_code=status.HTTP_201_CREATED)
async def generate_route(
    request: RouteGenerateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Generate route using AI agent."""
    ai_agent = AIRouteAgent()
    
    # Generate route using AI
    route_data = await ai_agent.generate_route(
        city=request.city,
        start_date=request.start_date,
        end_date=request.end_date,
        interests=request.interests,
        max_locations_per_day=request.max_locations_per_day,
        preferred_start_time=request.preferred_start_time,
        preferred_transport=request.preferred_transport,
    )
    
    # Create route in database
    route = Route(
        user_id=current_user.id,
        title=route_data["title"],
        description=route_data["description"],
        city=route_data["city"],
        start_date=route_data["start_date"],
        end_date=route_data["end_date"],
        interests=route_data["interests"],
    )
    
    db.add(route)
    db.commit()
    db.refresh(route)
    
    return route


@router.get("/", response_model=List[RouteSchema])
async def read_routes(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Get current user's routes."""
    routes = (
        db.query(Route)
        .filter(Route.user_id == current_user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    
    return routes


@router.get("/{route_id}", response_model=RouteSchema)
async def read_route(
    route_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Get route by ID."""
    route = db.query(Route).filter(Route.id == route_id).first()
    
    if not route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Route not found",
        )
    
    # Check if user has access
    if route.user_id != current_user.id and not route.is_public:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    
    return route


@router.put("/{route_id}", response_model=RouteSchema)
async def update_route(
    route_id: int,
    route_in: RouteUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Update route."""
    route = db.query(Route).filter(Route.id == route_id).first()
    
    if not route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Route not found",
        )
    
    if route.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    
    # Update fields
    update_data = route_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(route, field, value)
    
    db.commit()
    db.refresh(route)
    
    return route


@router.delete("/{route_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_route(
    route_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> None:
    """Delete route."""
    route = db.query(Route).filter(Route.id == route_id).first()
    
    if not route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Route not found",
        )
    
    if route.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
    
    db.delete(route)
    db.commit()


@router.get("/public/", response_model=List[RouteSchema])
async def read_public_routes(
    skip: int = 0,
    limit: int = 100,
    city: str = None,
    db: Session = Depends(get_db),
) -> Any:
    """Get public routes."""
    query = db.query(Route).filter(Route.is_public == True)
    
    if city:
        query = query.filter(Route.city == city)
    
    routes = query.offset(skip).limit(limit).all()
    
    return routes

