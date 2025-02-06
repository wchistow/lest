from json import dumps
from time import perf_counter
import traceback
from typing import Any, Callable, Literal, Optional
import xml.etree.ElementTree as ET

from rich.console import Console
from rich.table import Table


class Runner:
    """Runs all tests and report information about it."""
    def __init__(self) -> None:
        self.console = Console()  # for drawing

        # information
        self.successful = 0
        self.failed = 0
        self.elapsed = 0.0
        self.errors = 0

    def run(self, /, funcs: list[Callable], setup: Optional[Callable[..., Any]] = None,
            info_level: Literal['min', 'normal', 'max'] = 'normal',
            out_format: Literal['text', 'json', 'xml'] = 'text') -> None:
        if out_format == 'json':
            print('{')

        root = ET.Element('tests')

        for func in funcs:
            if info_level in ('normal', 'max') and out_format == 'text':
                print(f'Running [{func.__module__}.{func.__name__}]... ', end='')
            func_info = {}  # for JSON format
            start = perf_counter()
            if setup is not None:
                setup()
            try:
                func()
            except AssertionError:
                self.elapsed += perf_counter() - start
                if out_format == 'text':
                    if info_level == 'min':
                        self.console.print(f'[red]Test [{func.__module__}.{func.__name__}] FAILED:[/red]')
                        self.console.print(f'[red]{traceback.format_exc()}[/red]')
                    else:
                        self.console.print('[red]FAILED:[/red]')
                        self.console.print(f'[red]{traceback.format_exc()}[/red]')
                elif out_format == 'json':
                    func_info['status'] = 'failed'
                elif out_format == 'xml':
                    ET.SubElement(root, 'test', {'name': func.__module__ + '.' + func.__name__,
                                                 'status': 'failed'})
                self.failed += 1
            except:
                self.elapsed += perf_counter() - start
                if out_format == 'text':
                    if info_level == 'min':
                        self.console.print(f'[red]ERROR in [{func.__module__}.{func.__name__}]:[/red]')
                        self.console.print(f'[red]{traceback.format_exc()}[/red]')
                    else:
                        self.console.print('[red]ERROR:[/red]')
                        self.console.print(f'[red]{traceback.format_exc()}[/red]')
                elif out_format == 'json':
                    func_info['status'] = 'error'
                elif out_format == 'xml':
                    ET.SubElement(root, 'test', {'name': func.__module__ + '.' + func.__name__,
                                                 'status': 'error'})
                self.errors += 1
            else:
                self.elapsed += perf_counter() - start
                if out_format == 'text':
                    if info_level in ('normal', 'max'):
                        self.console.print('[green]OK[/green]')
                elif out_format == 'json':
                    func_info['status'] = 'ok'
                elif out_format == 'xml':
                    ET.SubElement(root, 'test', {'name': func.__module__ + '.' + func.__name__,
                                                 'status': 'ok'})
                self.successful += 1
            finally:
                if out_format == 'json':
                    if func is funcs[-1] and info_level != 'max':
                        print(f'  "{func.__module__}.{func.__name__}": {dumps(func_info)}')
                    else:
                        print(f'  "{func.__module__}.{func.__name__}": {dumps(func_info)},')

        total = self.successful + self.failed + self.errors

        if out_format == 'text':
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
        elif out_format == 'json':
            if info_level == 'max':
                result_info = {
                    'total': total,
                    'successful': self.successful,
                    'failed': self.failed,
                    'errors': self.errors,
                    'time elapsed': self.elapsed
                }
                print(f'  "<result>": {dumps(result_info)}')
            print('}')
        elif out_format == 'xml':
            ET.SubElement(root, 'result', {
                    'total': str(total),
                    'successful': str(self.successful),
                    'failed': str(self.failed),
                    'errors': str(self.errors),
                    'time_elapsed': '{:5.3f}'.format(self.elapsed)
                })
            ET.indent(root)
            print(ET.tostring(root, encoding='unicode'))

        if total != self.successful:  # some tests weren't successful
            exit(1)
        else:
            exit(0)
