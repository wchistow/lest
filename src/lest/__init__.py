import traceback

from rich.console import Console

from registerer import Registerer

register = Registerer()

console = Console()


def run():
    """Runs all tests and report information about it."""
    successful = 0
    failed = 0
    for func in register.funcs:
        print(f'Running [{func.__name__}]... ', end='')
        try:
            func()
        except AssertionError as e:
            console.print('[red]FAILED:[/red]')
            console.print(f'[red]{traceback.format_exc()}[/red]')
            failed += 1
        else:
            console.print('[green]OK[/green]')
            successful += 1

    print(f'Run {successful + failed} tests:')
    console.print(f'[green]   + Successful: {successful}[/green]')
    console.print(f'[red]   + Failed: {failed}[/red]')
