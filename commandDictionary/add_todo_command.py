from commandDictionary.command_struct import Command
from journalFunctions import add_todo
import textAnimations.blockReveal as blockReveal
import config


class AddEntryCommand(Command):
    name = "Add ToDo"
    aliases = ["addt"]

    def execute(self, args):
        task = input(blockReveal.openType("Enter task to add: "))
        dmod = 0
        for arg in args:
            try:
                dmod = int(arg)
                break
            except ValueError:
                pass

        add_todo.add_todo(dmod, task)

