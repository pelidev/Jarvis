import os
import sqlite3
from textAnimations import blockReveal
from pathlib import Path

DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
db_path = os.path.join(DB_BASE_DIR, "commonplace.db")

def tableName():
    while True:
        tablename = input("Please enter library name: ").strip()
        if tablename:
            return tablename.lower().replace(" ", "_")

        print("Library name cannot be blank")

def columnCollection():
    columns = []
    while True:
        columnname = input("Please enter column name (leave blank to finish): ").strip()
        if not columnname:
            break

        while True:
                columntype = input(f"What will '{columnname}' store: ").strip().upper()

                if not columntype:
                    columntype = "TEXT"  # blank input defaults
                    break
                elif columntype in ["TEXT", "INTEGER", "REAL", "BOOLEAN"]:
                    break
                else:
                    print("Invalid type. Please enter a valid type.")

        notnull = input(f"Should {columnname} be required? (y/n): ").strip().lower() == "y"
        columndef = f"{columnname} {columntype}" + (" NOT NULL" if notnull else "")
        columns.append(columndef)

    columns.append("date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    return columns

def createTable():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    parent_table_name = tableName()
    columns = columnCollection()

    sql = f"CREATE TABLE IF NOT EXISTS {parent_table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(columns)})"
    cur.execute(sql)

    childbuilder = input("Does this library need an additional table? (y/n): ").strip().lower() == "y"

    if childbuilder:
        child_table_name = f"{parent_table_name}_child"
        child_columns = columnCollection()
        fk_column = f"parent_id INTEGER NOT NULL"  # e.g., book_id
        fk_def = f"FOREIGN KEY (parent_id) REFERENCES {parent_table_name}(id)"
        child_columns.insert(0, fk_column)  # parent ID first
        child_columns.append(fk_def)
        sql = f"CREATE TABLE IF NOT EXISTS {child_table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(child_columns)})"
        cur.execute(sql)
        conn.commit()
        conn.close()
        blockReveal.openType(f"Created new Library '{parent_table_name}' with child system '{child_table_name}'.")
    else:
        conn.commit()
        conn.close()
        blockReveal.openType(f"Created new Library '{parent_table_name}'.")


