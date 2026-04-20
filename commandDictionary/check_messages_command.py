from emailFunctions import messagesjar
from commandDictionary.command_struct import Command


class CheckMessagesCommand(Command):
    name = "Check messages"
    aliases = ["cm"]

    def execute(self, args):
        messagesjar.check_Messages()



