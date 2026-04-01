from commandDictionary.command_struct import Command
from logFunctions import masterlog
from textAnimations.blockReveal import openType
import textAnimations.blockReveal as blockReveal
import config


class NmlogCommand(Command):
    name = "nmlog"
    aliases = ["nmlog"]

    def execute(self, args):
        if args:
            name = " ".join(args)
        else:
            name = input(blockReveal.openType("Log name: ")).strip()
            if not name:
                openType("Name cannot be empty.")
                return

        masterlog.new_masterlog(name)
        config.clearCheck = True
