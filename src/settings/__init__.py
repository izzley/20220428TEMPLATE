from loguru import logger
import sys

# logger configuration called from main
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "<yellow>{time:YYYY-MM-DD at HH:mm:ss}</> | <level>{level}</level>    | <green>{module}</>:<green>{function}</>:<green>{line}</> - <blue>{message}</> | {elapsed.seconds}"},
        {"sink": "src/logs/file.log", "serialize": True},
    ],
    "extra": {"user": "iz"},
}
logger.configure(**config)
logger.success("Logger setup from src/settings/__init__.py")

if __name__ == "__main__":
    logger.debug(f"Message test: {1+1}")