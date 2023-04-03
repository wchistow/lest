import traceback

from rich.console import Console

from registerer import Registerer

register = Registerer()

console = Console()


def run():
    """Runs all tests and report information about it."""
    for func in register.funcs:
        print(f"Running [{func.__name__}]... ", end='')
        try:
            func()
        except AssertionError as e:
            console.print("[red]FAILED:[/red]")
            console.print(f"[red]{traceback.format_exc()}[/red]")
        else:
            console.print("[green]OK[/green]")
