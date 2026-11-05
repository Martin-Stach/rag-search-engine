
import json
import os
from typing import TypedDict


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")


DEFAULT_SEARCH_LIMIT = 5

class Movie(TypedDict):
    id: int
    title: str
    description: str


def load_movies() -> list[Movie]:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]