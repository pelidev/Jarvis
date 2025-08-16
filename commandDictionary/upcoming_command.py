from commandDictionary.command_struct import Command
from combFunctions import openTasks
from textAnimations.blockReveal import openType
import config


class past_incomplete_command(Command):
    name = "upcoming"
    aliases = ["upc"]

    def execute(self, args):
        dmod = 0
        for arg in args:
            try:
                dmod = int(arg)
                break
            except ValueError:
                pass

        collection = openTasks.upcomingtasks(dmod)
        for task in collection:
            openType(task)


        config.clearCheck = False