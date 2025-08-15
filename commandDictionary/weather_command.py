from commandDictionary.command_struct import Command
from textAnimations import blockReveal
from weatherCalls import weatherjar
import config

class WeatherCommand(Command):
    name = "weather"
    aliases = ["w"]

    def execute(self,args):
        blockReveal.openType(weatherjar.showWeather(48160))
        config.clearCheck = False


