from typing import Iterable, Type


class assert_raises:
    def __init__(self, err: Type[Exception], /, message: str = ''):
        self.err = err
        self.message = message

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            assert issubclass(exc_type, self.err), self.message
        else:
            assert False, self.message
        return True


def assert_true(exp, /, message: str = ''):
    assert bool(exp), message


def assert_false(exp, /, message: str = ''):
    assert not bool(exp), message


def assert_eq(first, second, /, message: str = ''):
    assert first == second, message


def assert_in(it: Iterable, elem, /, message: str = ''):
    assert elem in it, message


def assert_not_in(it: Iterable, elem, /, message: str = ''):
    assert elem not in it, message
