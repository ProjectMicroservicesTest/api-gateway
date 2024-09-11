from typing import Optional, Any
from functools import wraps

from fastapi import HTTPException, Request, Response
from faststream.rabbit import RabbitBroker
from starlette import status

from src.app.infrastructure.brokers.rabbit_broker import rabbit
from src.app.main.config import RabbitConfig



def router(
    method,
    path: str,
    data_key: Optional[str] = None,
    status_code: Optional[int] = status.HTTP_200_OK,
    response_model: Optional[Any] = None,
):

    app_method = method(
        path, status_code=status_code, response_model=response_model
    )

    def wrapper(endpoint):
        @app_method
        @wraps(endpoint)
        async def decorator(request: Request, response: Response, **kwargs):
            request_method = request.scope["method"].lower()
            data = kwargs.get(data_key)
            data = data.dict() if data else {}
            response_data, response_status_code = await rabbit.publish(
                queue='/make-request',
                message={
                    "method": request_method,
                    "path": request.scope["path"],
                    "params": dict(request.query_params),
                    "data": data,
                    "headers": {},
                }, 
                rpc=True,
                rpc_timeout=3.5
            )
            if response_status_code >= status.HTTP_400_BAD_REQUEST:
                raise HTTPException(
                    status_code=response_status_code, detail=response_data
                )
            response.status_code = response_status_code
            return response_data

    return wrapper