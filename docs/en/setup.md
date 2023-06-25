# Writing setup

Setup - it's a function with the `@lest.setup` decorator.

It is called before each test.

Example:

```python
import lest


@lest.setup
def my_setup():
    print('Setuping...')


...  # Some tests
```
