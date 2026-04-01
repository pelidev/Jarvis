from commandDictionary.command_struct import Command
from readJar import book_reader
import config


class ResumeCommand(Command):
    name = "resume"
    aliases = ["res"]

    def execute(self, args):
        book_reader.resume_last_book()
        config.clearCheck = True
