import logging

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.propagate = False

logging.basicConfig(
    format = '{levelname}: {message}', 
    style = '{', 
    level = logging.INFO
)

logger = logging.getLogger(__name__)