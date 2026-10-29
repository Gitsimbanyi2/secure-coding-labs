"""Secure query helper. Bind parameters — never format SQL with user strings."""
import sqlite3
from pathlib import Path


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:" if db_path is None else db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, display TEXT)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO users (username, display) VALUES (?, ?)",
        ("labuser", "O'Brien"),
    )
    conn.commit()
    return conn


def find_user(conn: sqlite3.Connection, username: str) -> tuple | None:
    # INSECURE (do not use):
    #   conn.execute(f"SELECT * FROM users WHERE username = '{username}'")
    cur = conn.execute("SELECT id, username, display FROM users WHERE username = ?", (username,))
    return cur.fetchone()
