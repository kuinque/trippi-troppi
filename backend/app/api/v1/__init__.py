"""API v1 router."""

from fastapi import APIRouter

from app.api.v1.routes import auth, users, routes, locations, recommendations

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(routes.router, prefix="/routes", tags=["routes"])
api_router.include_router(locations.router, prefix="/locations", tags=["locations"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])

