import os
import sqlite3
from pathlib import Path

DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
db_path = os.path.join(DB_BASE_DIR, "commonplace.db")

def initDB():

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Global tags system
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS content_tags (
            content_type TEXT,   -- table name
            content_id INTEGER,  -- row id from that table
            tag_id INTEGER,
            FOREIGN KEY(tag_id) REFERENCES tags(id)
        )
        """)

    conn.commit()
    conn.close()
    return db_path