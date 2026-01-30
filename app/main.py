from fastapi import FastAPI

from app.api import characters, monsters, game_data
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    debug=settings.debug,
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the D&D API",
        "environment": settings.environment,
        "version": settings.api_version,
    }


# Include routers
app.include_router(characters.router)
app.include_router(monsters.router)
app.include_router(game_data.router)
