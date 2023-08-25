from typing import Callable, Optional


class Setup:
    def __init__(self):
        self.func: Optional[Callable] = None

    def __call__(self, func: Callable):
        self.func = func
        return func
