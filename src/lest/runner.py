from time import perf_counter
import traceback
from typing import Callable

from rich.console import Console


class Runner:
    """Runs all tests and report information about it."""
    def __init__(self):
        self.console = Console()  # for drawing

        # information
        self.successful = 0
        self.failed = 0
        self.elapsed = 0

    def run(self, funcs: list[Callable]) -> None:
        for func in funcs:
            print(f'Running [{func.__name__}]... ', end='')
            start = perf_counter()
            try:
                func()
            except AssertionError:
                self.elapsed += perf_counter() - start
                self.console.print('[red]FAILED:[/red]')
                self.console.print(f'[red]{traceback.format_exc()}[/red]')
                self.failed += 1
            else:
                self.elapsed += perf_counter() - start
                self.console.print('[green]OK[/green]')
                self.successful += 1

        print(f'Run {self.successful + self.failed} tests:')
        self.console.print(f'[green]   + Successful: {self.successful}[/green]')
        self.console.print(f'[red]   + Failed: {self.failed}[/red]')
        self.console.print('[blue]   + Time elapsed: {:5.3f}[/blue]'.format(self.elapsed))
