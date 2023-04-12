from typing import Iterable


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
