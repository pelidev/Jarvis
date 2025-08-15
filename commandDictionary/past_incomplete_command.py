from commandDictionary.command_struct import Command
from combFunctions import openTasks
import config

class past_incomplete_command(Command):
    name = "past_incomplete"
    aliases = ["inc"]

    def execute(self, args):
        dmod = 0
        for arg in args:
            try:
                dmod = int(arg)
                break
            except ValueError:
                pass

        collection = openTasks.incompletetasks(dmod)
        for task in collection:
            print(task)

        config.clearCheck = False