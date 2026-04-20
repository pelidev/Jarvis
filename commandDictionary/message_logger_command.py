from commandDictionary.command_struct import Command
from emailFunctions import messagesjar

class MessageLoggerCommand(Command):
    name = "Message Logger"
    aliases = ["smslog"]

    def execute(self, args):
        sms = " ".join(args) if args else "Blank text fired."
        messages = messagesjar.mjson_Loader()
        messages["messages"].append(sms)
        messagesjar.mjson_Writer(messages)