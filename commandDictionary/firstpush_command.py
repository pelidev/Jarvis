from commandDictionary.command_struct import Command
from pushCut.upcWidget import send_UPC
import config

class FirstPush(Command):
    name = "UPCWidget"
    aliases = ["wupc"]

    def execute(self, args):

        print("Widget updated!")
        send_UPC()
        config.clearCheck = True
