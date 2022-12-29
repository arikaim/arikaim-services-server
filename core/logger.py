import logging

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.propagate = False

logging.basicConfig(
    format = '{levelname:7} {message}', 
    style = '{', 
    level = logging.INFO
)

logger = logging.getLogger(__name__)