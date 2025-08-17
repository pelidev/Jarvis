from commandDictionary.command_struct import Command
from pathlib import Path
import config
import subprocess

JOURNAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "Journals"

class OpenCommand(Command):
    name = "open"
    aliases = ["op"]

    def execute(self, args):
        if not args:
            print("Please provide a date YYYY-MM-DD")
            return

        filename = args[0] + ".txt"

        matches = list(JOURNAL_BASE_DIR.rglob(filename))

        if not matches:
            print("Unable to locate file")
            print("Please try again.")
            config.clearCheck = False
            return

        file_to_open = matches[0]

        subprocess.run(["nvim", str(file_to_open)])

        config.clearCheck = True