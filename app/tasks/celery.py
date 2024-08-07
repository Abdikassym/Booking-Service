from celery import Celery
from app.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["app.tasks.tasks"]
)

celery.conf.update(
    broker_connection_retry_on_startup=True,  # Включаем повторные попытки подключения при старте
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
)