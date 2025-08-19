from commandDictionary.command_struct import Command
from databaseFunctions import entry_handler
import config

class AddEntryCommand(Command):
    name = "Add Entry"
    aliases = ["ae"]

    def execute(self, args):
        entry_handler.add_entry()
        config.clearCheck = True