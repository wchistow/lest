import traceback

from registerer import Registerer

register = Registerer()


def run():
    """Runs all tests and report information about it."""
    for func in register.funcs:
        print(f"Running [{func.__name__}]... ", end='')
        try:
            func()
        except AssertionError as e:
            print("FAILED:")
            traceback.print_exc()
        else:
            print("OK")
