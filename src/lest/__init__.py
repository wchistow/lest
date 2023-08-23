from functools import partial

from .assertions import *
from .registerer import Registerer
from .runner import Runner
from .setup import Setup

_registerer = Registerer()
_runner = Runner()
_setuper = Setup()

register = _registerer.__call__
run = partial(_runner.run, _registerer.funcs, setup=_setuper.func)
setup = _setuper.__call__

__all__ = ['register', 'run', 'setup',
           'assert_eq', 'assert_false', 'assert_in', 'assert_not_in', 'assert_raises']
