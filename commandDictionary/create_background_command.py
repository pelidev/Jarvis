from commandDictionary.command_struct import Command
from drawFunctions.bgbuilder import createBackground

class CreateBackgroundCommand(Command):
    name = "create_background"
    aliases = ["cb"]

    def execute(self,args):
        createBackground()