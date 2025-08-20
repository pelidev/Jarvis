
def list_table_names(conn, exclude_substrings=("tag", "sqlite_sequence", "child")):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names = [r[0] for r in cur.fetchall()]
    lower_excl = tuple(s.lower() for s in exclude_substrings)
    return [n for n in names if all(s not in n.lower() for s in lower_excl)]

def list_entries_by_name(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    entries = [r[1] for r in cursor.fetchall()]
    return entries

def entry_tuple_return(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    entries = [r for r in cursor.fetchall()]
    return entries

def parent_id_return(conn, table_name, parent_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    entries = cursor.fetchall()
    selected_id = next((r[0] for r in entries if r[1] == parent_name), None)
    return str(selected_id)

