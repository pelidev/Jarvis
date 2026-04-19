from commandDictionary.command_struct import Command
import config
from textAnimations import blockReveal

class HelpCommand(Command):

    name = "Help"
    aliases = ["help"]

    def execute(self, args):
        print("Journal functions:")
        print("  'DL' = Open current day log. [Add +/- int to modify day]")
        print("  'UPC' = Upcoming open tasks from daily logs. [Add +/- int to modify day range]")
        print("  'INC' = Previously incomplete tasks from daily logs. [Add +/- int to modify day range]")
        print("  'OP' = Open specific log date - argument required YYYY-MM-DD.")
        print("Database Functions:")
        print("  'CL' = Create new database library.")
        print("  'AE' = Add new parent category to a database.")
        print("  'AL' = Add new entry to a parent category. (Add quote to a book in the database.)")
        print("EReader:")
        print("  'ARES' = Active reader resume last book. [Add # of paragraphs to load]")
        print("  'AREAD' = Reader book selector.")
        print("  'RES' = NVIM Read resumer.")
        print("  'READ' = NVIM Select book to read.")
        print("  'IMPORT' = Import new MD's from markdowns folder.")
        print("Log Files:")
        print("  'MLOG' = List current logs.")
        print("  'NMLOG' = Create new master log.")
        print("Other:")
        print("  'Weather' = Weather readout.")
        config.clearCheck = False
