import os

import pytest

# uses Requests to make requests against the FastAPI app
from starlette.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get('DATABASE_TEST_URL'))



# dependency_overrides is a dict of key/value pairs where 
# the key is the dependency name and the value is what we'd like to override it with:
# key: get_settings
# value: get_settings_override
@pytest.fixture(scope='module')
def test_app():
    # set up / override dependencies
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client