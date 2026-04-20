#!/usr/bin/env python3
from dotenv import load_dotenv
from rich import box
from combFunctions.openTasks import upcomingtasks
load_dotenv()
from databaseFunctions import db_initializer
db_initializer.initDB()
from rich.table import Table
from rich.console import Console
import os
import config
import sys
from commandDictionary import command_registry
import journalFunctions.today as today
from emailFunctions import messagesjar



GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def dljump():
    today.open_today_journal(1, 0)


def main():
    # Table build
    console = Console()
    table = Table(expand=True, style="yellow", header_style="yellow", box=box.ROUNDED)
    table.add_column("[bold]Welcome back, Matthew", justify="left", style="yellow")

    # Statuses - ToDos
    incomplete = len(upcomingtasks(0, "_")) - 1
    complete = len(upcomingtasks(0, "X")) - 1

    if incomplete < 0:
        incomplete = 0

    if complete < 0:
        complete = 0

    if incomplete == 0 and complete == 0:
        table.add_row("No tasks scheduled for today.")

    else:
        table.add_row(f"Tasks left: {incomplete}")
        table.add_row(f"Tasks done: {complete}")

    # Statuses - Messages
    messages = messagesjar.mjson_Loader()
    if messages["messages"]:
        table.add_row(f"{len(messages['messages'])} New messages.")
    else:
        table.add_row("No new messages.")

    # Print table to console
    console.print(table)

    while True:
        try:
            if config.clearCheck:
                os.system('cls' if os.name == 'nt' else 'clear')

            user_input = input(f"{YELLOW}Jarvis> {RESET}").strip()
            if not user_input:
                continue

            parts = user_input.split()
            cmd_name, args = parts[0], parts[1:]

            command = command_registry.get(cmd_name)
            if command:
                try:
                    command.execute(args)
                except Exception as e:
                    print(f"{RED}Error executing command:{RESET} {e}")
            else:
                config.clearCheck = False
                print(f"{YELLOW}Unknown command:{RESET} {cmd_name}")

        except KeyboardInterrupt:
            print(f"\n{CYAN}Exiting Jarvis. Goodbye!{RESET}")
            break
        except Exception as e:
            print(f"{RED}Unexpected error:{RESET} {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd_name = sys.argv[1].lower()
        extra_args = sys.argv[2:]

        if cmd_name == "dljump":
            dljump()
        else:
            command = command_registry.get(cmd_name)
            if command:
                try:
                    command.execute(extra_args)
                except Exception as e:
                    print(f"{RED}Error executing command:{RESET} {e}")
            else:
                print(f"{YELLOW}Unknown command:{RESET} {cmd_name}")
    else:
        main()