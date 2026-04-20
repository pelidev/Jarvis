from rich import box
from pathlib import Path
import json
from rich.console import Console
from rich.table import Table

MESSAGES_FILE = Path(__file__).resolve().parent.parent.parent / "Jarvis_Data" / "messages.json"

def mjson_Loader():
    if MESSAGES_FILE.exists():
        with open(MESSAGES_FILE) as f:
            return json.load(f)
    return {"messages": []}

def mjson_Writer(messages):
    with open(MESSAGES_FILE, "w") as f:
        json.dump(messages, f, indent=2)


def check_Messages():
    console = Console()
    table = Table(style="yellow", box=box.ROUNDED)
    table.add_column("[bold]Messages:", style="yellow")
    messages = mjson_Loader()
    if messages["messages"]:
        for i in messages["messages"]:
            table.add_row(i)

        console.print(table)
        kord = input("Would you like to keep or delete? [K/D]").strip().lower()
        while True:
            if kord == "k":
                print("Messages kept!")
                break
            elif kord == "d":
                messages["messages"] = []
                mjson_Writer(messages)
                break
            else:
                print("Invalid input. Please try again.")

    else:
        print("No messages.")


