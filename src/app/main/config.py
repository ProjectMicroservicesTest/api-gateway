from pydantic_settings import BaseSettings
from pydantic import Field


class RabbitConfig(BaseSettings):
    host: str = Field("localhost", env="RABBIT_HOST")
    port: int = Field(5672, env="RABBIT_PORT")
    username: str = Field("guest", env="RABBIT_USER")
    password: str = Field("guest", env="RABBIT_PASSWORD")