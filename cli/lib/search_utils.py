
import json
import os
from typing import TypedDict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MOVIES_DATA_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOPWORDS_FILE_PATH = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")

DEFAULT_SEARCH_LIMIT = 5

class Movie(TypedDict):
    id: int
    title: str
    description: str


def load_movies() -> list[Movie]:
    with open(MOVIES_DATA_FILE_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

