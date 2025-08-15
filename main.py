#!/usr/bin/env python3
import os
import subprocess
import journalFunctions.today as today
import textAnimations.blockReveal as blockReveal
from dotenv import load_dotenv
load_dotenv()
import weatherCalls.weatherjar as weatherJar
import sys
#different
# ANSI color codes
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def dljump():
    today.open_today_journal(1, 0)

def main():
    blockReveal.blockReaveal(f"{GREEN}Welcome back, Matthew.{RESET}", 1)
    weatherNow = str(weatherJar.showWeather(48160))
    clearcheck = 0
    while True:
        try:
            if clearcheck != 0:
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                clearcheck += 1

        user_input = input("Jarvis> ").strip()
        if not user_input:
            continue

        parts = user_input.split()
        cmd_name, args = parts[0], parts[1:]

        command = command_registry.get(cmd_name)
        if command:
            try:
                command.execute(args)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {cmd_name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "dljump":
            dljump()
        else:
            print(f"Unknown command-line argument: {arg}")
    else:
        main()
