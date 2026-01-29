from fastapi import APIRouter
import json
from pathlib import Path

from app.models import MonstersResponse

router = APIRouter(prefix="/monsters", tags=["monsters"])


@router.get("", response_model=MonstersResponse)
def get_monsters():
    """Return all D&D monsters"""
    monsters_file = Path(__file__).parent.parent / "monsters.json"
    with open(monsters_file, "r") as f:
        monsters = json.load(f)
    return {"monsters": monsters}
