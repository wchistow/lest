from typing import Callable, Optional


class Setup:
    def __init__(self) -> None:
        self.func: Optional[Callable] = None

    def __call__(self, func: Callable) -> Callable:
        self.func = func
        return func
