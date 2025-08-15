from commandDictionary.command_struct import Command
from textAnimations import blockReveal
from weatherCalls import weatherjar

class WeatherCommand(Command):
    name = "weather"
    aliases = ["w"]

    def execute(self,args):
        blockReveal.openType(weatherjar.showWeather(48160))

