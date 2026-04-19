from commandDictionary.command_struct import Command
from journalFunctions import add_todo
import config

class MessageLoggerCommand(Command):
    name = "Message Logger"
    aliases = ["smslog"]

    def execute(self, args):
        task = " ".join(args) if args else "Blank text fired."
        add_todo.add_todo(0, task)