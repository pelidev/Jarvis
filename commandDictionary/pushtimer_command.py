from commandDictionary.command_struct import Command
from pushCut.phoneLock import timer_Push
import config

class PushTimer(Command):
    name = "PushTimer"
    aliases = ["pt"]

    def execute(self, args):
        description = input("Title: ").strip()
        duration = input("Duration: ").strip()
        timer_Push(description, duration)