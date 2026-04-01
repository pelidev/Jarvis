from commandDictionary.command_struct import Command
from readJar import book_reader
import config


class ReadCommand(Command):
    name = "read"
    aliases = ["read"]

    def execute(self, args):
        book_reader.list_and_open_book()
        config.clearCheck = True

