from fastapi import FastAPI
from faststream import FastStream
from contextlib import asynccontextmanager

from src.app.presentation.api.v1 import check_health_auth
from src.app.presentation.api.v1 import check_health_profile
from src.app.presentation.api.v1 import check_health_tasks
from src.app.infrastructure.brokers.rabbit_broker import rabbit


@asynccontextmanager
async def lifespan(app: FastAPI):
    fastsream = get_faststream_app()
    await fastsream.broker.start()
    yield


def get_fastapi_app(lifespan) -> FastAPI:
    app=FastAPI(lifespan=lifespan)
    app.include_router(check_health_auth.health_check_router)
    app.include_router(check_health_profile.health_check_router)
    app.include_router(check_health_tasks.health_check_router)
    return app

def get_faststream_app() -> FastStream:
    app=FastStream(rabbit)
    return app

def get_app():
    fastapi = get_fastapi_app(lifespan=lifespan)
    return fastapi
    


    
