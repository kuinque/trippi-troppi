"""Location routes."""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.location import Location
from app.schemas.location import Location as LocationSchema, LocationSearchRequest
from app.services.maps_service import open_trip_map, yandex_maps

router = APIRouter()


@router.post("/search", response_model=List[LocationSchema])
async def search_locations(
    search: LocationSearchRequest,
    db: Session = Depends(get_db),
) -> Any:
    """Search for locations."""
    # First, try to get from database
    query = db.query(Location).filter(Location.city == search.city)
    
    if search.category:
        query = query.filter(Location.category == search.category)
    
    if search.latitude and search.longitude and search.radius:
        # TODO: Add geospatial query
        pass
    
    locations = query.limit(search.limit).all()
    
    # If not enough results, fetch from external APIs
    if len(locations) < search.limit:
        # Fetch from OpenTripMap
        try:
            external_locations = await open_trip_map.get_places(
                city=search.city,
                kinds=search.category,
                limit=search.limit,
            )
            # TODO: Process and save to database
        except Exception as e:
            print(f"Error fetching from OpenTripMap: {e}")
    
    return locations


@router.get("/{location_id}", response_model=LocationSchema)
async def read_location(
    location_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """Get location by ID."""
    location = db.query(Location).filter(Location.id == location_id).first()
    
    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Location not found",
        )
    
    return location


@router.get("/nearby/{latitude}/{longitude}", response_model=List[LocationSchema])
async def get_nearby_locations(
    latitude: float,
    longitude: float,
    radius: int = 1000,
    category: str = None,
    limit: int = 20,
    db: Session = Depends(get_db),
) -> Any:
    """Get nearby locations."""
    # TODO: Implement geospatial query
    # For now, return empty list
    
    try:
        # Fetch from OpenTripMap
        external_locations = await open_trip_map.search_radius(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            kinds=category,
            limit=limit,
        )
        
        # TODO: Process and save to database
        return []
    except Exception as e:
        print(f"Error fetching nearby locations: {e}")
        return []

