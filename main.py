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

            cmd = input(blockReveal.blockReaveal(f"{CYAN}Jarvis> {RESET}", 0)).strip()
            cmds = cmd.split()
            firstcmd = cmds[0].lower()
            if cmd.lower() in {"exit", "quit"}:
                print(f"{YELLOW}Goodbye.{RESET}")
                break

            elif firstcmd == "w":
                blockReveal.openType(weatherNow)
                clearcheck -= 1

            elif firstcmd == "dl":
                try:
                    secondcmd = int(cmds[1]) if len(cmds) > 1 else 0
                except ValueError:
                    secondcmd = 0

                if "micro" in cmd.lower():
                    today.open_today_journal(0, secondcmd)
                else:
                    today.open_today_journal(1, secondcmd)

            elif cmd.lower() == "pl jarvis":
                subprocess.run(["nano", "pl_jarvis.txt"])

            elif cmd:
                print(f"{GREEN}You said:{RESET} {cmd}")

        except KeyboardInterrupt:
            print(f"\n{RED}Interrupted. Exiting.{RESET}")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "dljump":
            dljump()
        else:
            print(f"Unknown command-line argument: {arg}")
    else:
        main()
