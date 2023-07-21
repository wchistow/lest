from typing import Iterable, Type


class assert_raises:
    def __init__(self, err: Type, /):
        self.err = err

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if not issubclass(exc_type, self.err):
                raise AssertionError(f'{exc_type} is not {self.err}.')
        else:
            raise AssertionError('no exception raised.')
        return True


def assert_true(exp, /):
    if not exp:
        raise AssertionError('expression is not \'True\'.')


def assert_false(exp, /):
    if exp:
        raise AssertionError('expression is not \'False\'.')


def assert_eq(first, second, /):
    if not (first == second):
        raise AssertionError(f'{repr(first)} != {repr(second)}.')


def assert_in(it: Iterable, elem, /):
    if elem not in it:
        raise AssertionError(f'{repr(elem)} not in given iterable object.')


def assert_not_in(it: Iterable, elem, /):
    if elem in it:
        raise AssertionError(f'{repr(elem)} in given iterable object.')
