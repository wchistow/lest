from .registerer import Registerer
from .runner import Runner
from .setup import Setup

_registerer = Registerer()
_runner = Runner()
_setuper = Setup()

register = _registerer.__call__
run = lambda: _runner.run(_registerer.funcs, setup=_setuper.func)
setup = _setuper.__call__

__all__ = ['register', 'run', 'setup']
