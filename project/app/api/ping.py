from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get('/ping')
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
