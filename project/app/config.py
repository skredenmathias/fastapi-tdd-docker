import logging
import os
from functools import lru_cache

# Validates the data so that when we create an instance of Settings/environment/testing
# they will have types of 'str' and 'bool' respectively
from pydantic import BaseSettings, AnyUrl

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    # defines the environment (dev, stage, prod)
    environment: str = os.getenv('ENVIRONMENT', 'dev')
    # defines whether or not we're in test mode
    testing: bool = os.getenv('TESTING', 0)
    # AnyUrl will attempt to give a descriptive error when invalid URL is provided
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


# lru_cache cahes the settings so 'get_settings' is only called once
@lru_cache()
def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment...')
    return Settings()
