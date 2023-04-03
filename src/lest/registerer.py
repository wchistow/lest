from typing import Callable


class Registerer:
    """Register test functions to run it."""
    def __init__(self):
        self.funcs: list[Callable] = []

    def __call__(self, func: Callable):
        """Decorator, that registers function."""
        self.funcs.append(func)
        return func
