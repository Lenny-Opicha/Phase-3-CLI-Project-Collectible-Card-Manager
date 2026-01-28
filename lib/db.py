import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "collectible_cards.db"

CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()