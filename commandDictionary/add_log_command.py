from commandDictionary.command_struct import Command
from databaseFunctions import entry_handler
import config

class AddLogCommand(Command):
    name = "Add Log"
    aliases = ["al"]


    def execute(self, args):
        entry_handler.add_child()
        config.clearCheck = False
