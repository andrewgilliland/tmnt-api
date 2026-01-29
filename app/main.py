from fastapi import FastAPI

from app.api import characters, monsters, game_data

app = FastAPI(title="D&D API")


@app.get("/")
def root():
    return {"message": "Welcome to the D&D API"}


# Include routers
app.include_router(characters.router)
app.include_router(monsters.router)
app.include_router(game_data.router)
