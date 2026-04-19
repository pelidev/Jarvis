from commandDictionary.command_struct import Command
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

JOURNAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Journals"

class SiriDlCommand(Command):
    name = "siridl"
    aliases = ["siridl"]

    def execute(self, args):
        dmod = 0
        for arg in args:
            try:
                dmod = int(arg)
                break
            except ValueError:
                pass

        now = datetime.now(ZoneInfo("America/Denver")) + timedelta(days=dmod)
        file = JOURNAL_BASE_DIR / now.strftime("%Y-%m") / now.strftime("%Y-%m-%d.txt")

        if not file.exists():
            print("No journal entry for that day.")
            return

        with open(file, "r") as f:
            for line in f:
                print(line, end="")