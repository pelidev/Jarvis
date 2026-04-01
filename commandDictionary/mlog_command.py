from commandDictionary.command_struct import Command
from logFunctions import masterlog
import config


class MlogCommand(Command):
    name = "mlog"
    aliases = ["mlog"]

    def execute(self, args):
        masterlog.open_masterlog()
        config.clearCheck = True
