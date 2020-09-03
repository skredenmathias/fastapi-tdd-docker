import os

import pytest
# uses Requests to make requests against the FastAPI app
from starlette.testclient import TestClient

from tortoise.contrib.fastapi import register_tortoise

from app.main import create_application
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get('DATABASE_TEST_URL'))


# dependency_overrides is a dict of key/value pairs where
# the key is the dependency name and the value is what we'd like to override it with:
# key: get_settings
# value: get_settings_override
@pytest.fixture(scope='module')
def test_app_with_db():
    # set up / override dependencies
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        # testing
        yield test_client
