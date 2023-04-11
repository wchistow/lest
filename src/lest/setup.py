from typing import Callable


class Setup:
    def __init__(self):
        self.func: Callable | None = None

    def __call__(self, func: Callable):
        self.func = func
