from commandDictionary.command_struct import Command
from readJar import active_reader
import config


class AreadCommand(Command):
    name = "aread"
    aliases = ["aread"]

    def execute(self, args):
        lines_per_page = 5
        for arg in args:
            try:
                lines_per_page = int(arg)
                break
            except ValueError:
                pass

        active_reader.active_read_select(lines_per_page)
        config.clearCheck = True
