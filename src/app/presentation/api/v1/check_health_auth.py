from typing import List

from fastapi import APIRouter, Response
from fastapi.params import Query
from starlette import status
from starlette.requests import Request

from src.app.presentation.api.router import router

health_check_router = APIRouter(prefix = '/auth', tags=["health-check"])


@router(
    method=health_check_router.get,
    path='/health-check',
)
async def health_check_auth(request: Request, response: Response):
    pass