#!/usr/bin/env python3
import os
import textAnimations.blockReveal as blockReveal
import sys
from commandDictionary import command_registry
import journalFunctions.today as today
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

    clearcheck = False
    blockReveal.blockReaveal(f"{GREEN}Welcome back, Matthew.{RESET}", 1)

    while True:
        try:
            # Clear screen after the first iteration
            if clearcheck == True:
                os.system('cls' if os.name == 'nt' else 'clear')

            else:
                pass

            user_input = input(blockReveal.blockReaveal(f"{CYAN}Jarvis> {RESET}", 0)).strip()
            if not user_input:
                continue

            parts = user_input.split()
            cmd_name, args = parts[0], parts[1:]

            command = command_registry.get(cmd_name)
            if command:
                try:
                    command.execute(args)
                    clearcheck = True
                except Exception as e:
                    print(f"{RED}Error executing command:{RESET} {e}")
            else:
                clearcheck -= 1
                print(f"{YELLOW}Unknown command:{RESET} {cmd_name}")

        except KeyboardInterrupt:
            print(f"\n{CYAN}Exiting Jarvis. Goodbye!{RESET}")
            break
        except Exception as e:
            print(f"{RED}Unexpected error:{RESET} {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "dljump":
            dljump()
        else:
            print(f"{YELLOW}Unknown command-line argument:{RESET} {arg}")
    else:
        main()
