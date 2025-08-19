import sqlite3
import os
from pathlib import Path

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.document import Document

# ---------- paths ----------
DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
os.makedirs(DB_BASE_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_BASE_DIR, "commonplace.db")


# ---------- helpers ----------
def list_tables(conn, exclude_substrings=("tag", "sqlite_sequence", "child")):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names = [r[0] for r in cur.fetchall()]
    lower_excl = tuple(s.lower() for s in exclude_substrings)
    return [n for n in names if all(s not in n.lower() for s in lower_excl)]

def list_entries(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    entries = cursor.fetchall()
    conn.close()
    return entries


def single_line_selector(message: str, options: list[str]) -> str:
    if not options:
        raise ValueError("No options to select from.")

    session = PromptSession()
    kb = KeyBindings()
    idx = 0  # start at first option

    def _set_text(event, text: str):
        buf = event.app.current_buffer
        buf.set_document(Document(text=text, cursor_position=len(text)))

    @kb.add("up")
    def _(event):
        nonlocal idx
        idx = (idx - 1) % len(options)
        _set_text(event, options[idx])

    @kb.add("down")
    def _(event):
        nonlocal idx
        idx = (idx + 1) % len(options)
        _set_text(event, options[idx])

    # prefill input with first option; arrows will swap it
    return session.prompt(f"{message} ", default=options[idx], key_bindings=kb, complete_while_typing=False)


# ---------- command ----------
def add_entry():
    conn = sqlite3.connect(DB_PATH)
    try:
        tables = list_tables(conn)
        if not tables:
            print("No user tables found.")
            return

        table_name = single_line_selector("Select a library:", tables)

        # pull column names (skip id/date_added)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table_name})")
        cols = [c[1] for c in cur.fetchall() if c[1] not in ("id", "date_added")]

        if not cols:
            print(f"No editable columns in '{table_name}'.")
            return

        # prompt values
        vals = []
        for col in cols:
            vals.append(input(f"{col}> ").strip() or None)

        placeholders = ", ".join("?" for _ in cols)
        sql = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({placeholders})"
        cur.execute(sql, vals)
        conn.commit()
        print(f"Inserted new entry into '{table_name}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    add_entry()
