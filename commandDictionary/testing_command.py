from commandDictionary.command_struct import Command
from rich.table import Table
from rich import box
from rich.console import Console
from rich.panel import Panel

class CommandDictionary(Command):
    name = "Tester"
    aliases = ["test"]

    def execute(self, args):
        table = Table(box=box.HORIZONTALS)

        text = Panel.fit("[bold]Hello World", style="yellow")

        table.add_column("Command", justify="right", style="cyan")
        table.add_column("Description", justify="right", style="green")
        table.add_column("Arguments", justify="right", style="blue")

        table.add_row("ARES", "Active resume last read book.", "# of paragraphs per queue.")
        table.add_row("MLOG", "List masterlogs.", "None")
        table.add_row("DL", "Open daily journal entry.", "+/- days")

        console = Console()
        console.print(text)
        console.print(table)