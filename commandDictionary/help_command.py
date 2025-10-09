from commandDictionary.command_struct import Command
import config
from textAnimations import blockReveal

class HelpCommand(Command):

    name = "Help"
    aliases = ["help"]

    def execute(self, args):
        blockReveal.openType("Journal functions:")
        blockReveal.openType("'DL' = Open current day log. [Add +/- int to modify day]")
        blockReveal.openType("'UPC' = Upcoming open tasks from daily logs. [Add +/- int to modify day range]")
        blockReveal.openType("'INC' = Previously incomplete tasks from daily logs. [Add +/- int to modify day range]")
        blockReveal.openType("'OP' = Open specific log date - argument required YYYY-MM-DD.")
        blockReveal.openType("Database Functions:")
        blockReveal.openType("'CL' = Create new database library.")
        blockReveal.openType("'AE' = Add new parent category to a database.")
        blockReveal.openType("'AL' = Add new entry to a parent category. (Add quote to a book in the database.)")
        blockReveal.openType("Other:")
        blockReveal.openType("'Weather' = Weather readout.")
        config.clearCheck = False
