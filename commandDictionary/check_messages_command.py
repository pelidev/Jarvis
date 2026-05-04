from emailFunctions import messagesjar
from commandDictionary.command_struct import Command
import config


class CheckMessagesCommand(Command):
    name = "Check messages"
    aliases = ["cm"]

    def execute(self, args):
        messagesjar.check_Messages()
        config.clearCheck = False



