# Writing basic test

Test - it's just a function decorated by `@lest.register` decorator.

To test any behavior, use the `assert` keyword.

To run all tests, just call the `lest.run()` function.

Example:

```python
import lest


@lest.register  # using of the `@lest.register` decorator
def test_add_two_and_two():
    assert 2 + 2 == 4


lest.run()  # Calling `lest.run` function
```
