from time import perf_counter
import traceback
from typing import Callable, Literal, Any

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
        self.errors = 0

    def run(self, /, funcs: list[Callable], setup: Callable[..., Any] | None = None,
            info_level: Literal['min', 'normal', 'max'] = 'normal') -> None:
        for func in funcs:
            if info_level in ('normal', 'max'):
                print(f'Running [{func.__module__}.{func.__name__}]... ', end='')
            start = perf_counter()
            if setup is not None:
                setup()
            try:
                func()
            except AssertionError:
                self.elapsed += perf_counter() - start
                if info_level == 'min':
                    self.console.print(f'[red]Test [{func.__module__}.{func.__name__}] FAILED:[/red]')
                    self.console.print(f'[red]{traceback.format_exc()}[/red]')
                else:
                    self.console.print('[red]FAILED:[/red]')
                    self.console.print(f'[red]{traceback.format_exc()}[/red]')
                self.failed += 1
            except:
                self.elapsed += perf_counter() - start
                if info_level == 'min':
                    self.console.print(f'[red]ERROR in [{func.__module__}.{func.__name__}]:[/red]')
                    self.console.print(f'[red]{traceback.format_exc()}[/red]')
                else:
                    self.console.print('[red]ERROR:[/red]')
                    self.console.print(f'[red]{traceback.format_exc()}[/red]')
                self.errors += 1
            else:
                self.elapsed += perf_counter() - start
                if info_level in ('normal', 'max'):
                    self.console.print('[green]OK[/green]')
                self.successful += 1

        total = self.successful + self.failed + self.errors

        if info_level == 'max':
            result_table = Table(title='Tests stats')

            result_table.add_column('Total tests', style='blue')
            result_table.add_column('Successful', style='green')
            result_table.add_column('Failed', style='red')
            result_table.add_column('Errors', style='red')
            result_table.add_column('Time elapsed', style='white')

            result_table.add_row(str(total),
                                 str(self.successful),
                                 str(self.failed),
                                 str(self.errors),
                                 '{:5.3f}'.format(self.elapsed))

            self.console.print(result_table)
        else:
            if total == self.successful:
                self.console.print(f'[green]Passed {self.successful}/{total} tests[/green]')
            else:
                self.console.print(f'[red]Passed {self.successful}/{total} tests[/red]')

        if total != self.successful:  # some tests weren't successful
            exit(1)
        else:
            exit(0)
