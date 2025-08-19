from commandDictionary.command_struct import Command
from databaseFunctions import table_creation
import config

class createLibrary(Command):
    name = "create library"
    aliases = ["cl"]

    def execute(self, args):
        table_creation.createTable()
        config.clearCheck = False

