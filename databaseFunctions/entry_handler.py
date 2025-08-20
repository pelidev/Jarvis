import sqlite3
import os
from pathlib import Path
from databaseFunctions import db_caller
from textAnimations import menu_animations
from databaseFunctions import db_dynamic_entry

# ---------- paths ----------
DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
os.makedirs(DB_BASE_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_BASE_DIR, "commonplace.db")

def add_child():
    conn = sqlite3.connect(DB_PATH)

    # ------------------ Table Selector
    tables = db_caller.list_table_names(conn)
    if not tables:
        print("No user tables found.")
        return

    parent_table_name = menu_animations.single_line_selector("Select a library:", tables)

    # --------------- Listing selector

    volume_names = db_caller.list_entries_by_name(conn, parent_table_name)
    if not volume_names:
        print("No volumes available, please create one.")
        return

    entry_selected = menu_animations.single_line_selector("Select a volume:", volume_names)
    parent_id = db_caller.parent_id_return(conn, parent_table_name, entry_selected)

    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({parent_table_name}_child)")
    cols_info = [c for c in cur.fetchall() if c[1] not in ("id", "date_added", "parent_id")]

    if not cols_info:
        print(f"No editable columns in '{parent_table_name}'.")
        return

    vals = db_dynamic_entry.prompt_for_columns(cols_info)

    col_names = [c[1] for c in cols_info]
    col_names.append("parent_id")
    vals.append(parent_id)
    placeholders = ", ".join("?" for _ in col_names)
    sql = f"INSERT INTO {parent_table_name}_child ({', '.join(col_names)}) VALUES ({placeholders})"

    cur.execute(sql, vals)
    conn.commit()

    print("Huzzah")



def add_entry():
    conn = sqlite3.connect(DB_PATH)
    try:
        tables = db_caller.list_table_names(conn)
        if not tables:
            print("No user tables found.")
            return

        table_name = menu_animations.single_line_selector("Select a library:", tables)

        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table_name})")
        cols_info = [c for c in cur.fetchall() if c[1] not in ("id", "date_added")]

        if not cols_info:
            print(f"No editable columns in '{table_name}'.")
            return

        # prompt for values
        vals = db_dynamic_entry.prompt_for_columns(cols_info)

        # build INSERT statement
        col_names = [c[1] for c in cols_info]
        placeholders = ", ".join("?" for _ in col_names)
        sql = f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({placeholders})"

        cur.execute(sql, vals)
        conn.commit()
        print(f"Inserted new entry into '{table_name}'.")
    finally:
        conn.close()
