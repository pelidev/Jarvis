from commandDictionary.command_struct import Command
from journalFunctions import today

class DlCommand(Command):
    name = "journal"
    aliases = ["dl"]

    def execute(self, args):
        dmod = 0
        for arg in args:
            try:
                dmod = int(arg)
                break
            except ValueError:
                pass

        if "micro" in args:
            today.open_today_journal(0,dmod)
        else:
            today.open_today_journal(1,dmod)


