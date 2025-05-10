import logging
import os
from .config import Config


def create_logger():
    os.makedirs(Config.LOGS_DIR_PATH, exist_ok=True)

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = False

    return logger


logger = create_logger()
