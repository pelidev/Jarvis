from commandDictionary.command_struct import Command
from readJar import import_books
import config


class ImportMdsCommand(Command):
    name = "importmds"
    aliases = ["importmds"]

    def execute(self, args):
        import_books.import_markdowns()
        config.clearCheck = False
