from typing import Callable


class Registerer:
    """Register test functions to run it."""
    def __init__(self) -> None:
        self.funcs: list[Callable] = []

    def __call__(self, func: Callable) -> Callable:
        """Decorator, that registers function."""
        self.funcs.append(func)
        return func
