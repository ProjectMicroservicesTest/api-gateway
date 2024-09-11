from fastapi import APIRouter, Response
from starlette.requests import Request

from src.app.presentation.api.router import router

health_check_router = APIRouter(prefix="/profile", tags=["health-check"])


@router(
    method=health_check_router.get,
    path='/health-check',
)
async def health_check_profile(request: Request, response: Response):
    pass