from commandDictionary.command_struct import Command
from combFunctions import openTasks
import config
from textAnimations.blockReveal import openType


class past_incomplete_command(Command):
    name = "upcoming"
    aliases = ["upc, tod"]

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