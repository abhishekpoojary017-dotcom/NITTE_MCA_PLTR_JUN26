import sqlite3
import os


DB_PATH = os.environ.get("DB_NAME", "hostel_db.sqlite")


def get_connection():
    """Return a sqlite3 connection. Uses `DB_NAME` env var or defaults to `hostel_db.sqlite`."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
