from fastapi import APIRouter
import json
from pathlib import Path

from app.models import CharactersResponse

router = APIRouter(prefix="/characters", tags=["characters"])


@router.get("", response_model=CharactersResponse)
def get_characters():
    """Return all D&D characters from Dragonlance"""
    characters_file = Path(__file__).parent.parent / "characters.json"
    with open(characters_file, "r") as f:
        characters = json.load(f)
    return {"characters": characters}
