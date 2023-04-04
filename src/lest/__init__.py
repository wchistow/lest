from .registerer import Registerer
from .runner import Runner

registerer = Registerer()
runner = Runner()

register = registerer.__call__
run = lambda: runner.run(registerer.funcs)

__all__ = ['register', 'run']
