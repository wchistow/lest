import lest


@lest.setup
def my_setup():
    print('Setup ran!')


@lest.register
def test_adding_two_and_two():
    lest.assert_eq(2 + 2, 4)


@lest.register
def some_error_test():
    lest.assert_eq(2 + 2, 5)  # AssertionError


@lest.register
def some_more_error():
    lest.assert_eq(a + 2, 4)  # NameError


lest.run(info_level='max')
