from commandDictionary.command_struct import Command
import os
from pathlib import Path
import sqlite3
from databaseFunctions import entry_handler
import config

class AddLogCommand(Command):
    name = "Add Log"
    aliases = ["al"]

    DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
    os.makedirs(DB_BASE_DIR, exist_ok=True)
    DB_PATH = os.path.join(DB_BASE_DIR, "commonplace.db")

    def execute(self, args):
        DB_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Database"
        os.makedirs(DB_BASE_DIR, exist_ok=True)
        DB_PATH = os.path.join(DB_BASE_DIR, "commonplace.db")

        conn = sqlite3.connect(DB_PATH)
        entry_handler.add_child()
        config.clearCheck = False
