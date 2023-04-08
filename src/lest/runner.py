from time import perf_counter
import traceback
from typing import Callable

from rich.console import Console
from rich.table import Table


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

        result_table = Table(title='Tests stats')

        result_table.add_column('Total tests', style='blue')
        result_table.add_column('Successful', style='green')
        result_table.add_column('Failed', style='red')
        result_table.add_column('Time elapsed', style='white')

        result_table.add_row(str(self.successful + self.failed),
                             str(self.successful),
                             str(self.failed),
                             '{:5.3f}'.format(self.elapsed))

        self.console.print(result_table)
