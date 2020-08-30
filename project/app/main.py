import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise


from app.config import get_settings, Settings

app = FastAPI()

# Registers startup and shutdown events to set-up and tear-down
# Tortoise-ORM inside a FastAPI application.
# https://tortoise-orm.readthedocs.io/en/latest/contrib/fastapi.html#tortoise.contrib.fastapi.register_tortoise
register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



@app.get('/ping')
# 'Depends' function is a dependency that declares another dependeny, get settings
# Reworded: Depends depends on the result of 'get_settings'.
# the value returned, Settings, is then assgined to the 'settings' parameter
# https://fastapi.tiangolo.com/tutorial/dependencies/
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong!',
        'environment': settings.environment,
        'testing': settings.testing
        }