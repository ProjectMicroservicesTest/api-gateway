from faststream.rabbit import RabbitBroker
from faststream.security import SASLPlaintext

from src.app.main.config import RabbitConfig

def rabbit_broker(config: RabbitConfig) -> RabbitBroker:
    broker = RabbitBroker(
        host=config.host,
        port=config.port,
        security=SASLPlaintext(
            username=config.username,
            password=config.password,
        ),
        virtualhost='/'
    )
    return broker

rabbit = rabbit_broker(RabbitConfig())