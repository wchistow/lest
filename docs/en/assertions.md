# Using `assert`'s shortcuts

There are some useful functions in the lest library,
that replaces some common uses of the `assert` keyword:

| lest function                            | assert                            |
|------------------------------------------|-----------------------------------|
| `lest.assert_eq(first, second, message)` | `assert first == second, message` |
| `lest.assert_true(exp, message)`         | `assert exp, message`             |
| `lest.assert_false(exp, message)`        | `assert not exp, message`         |
| `lest.assert_in(it, elem, message)`      | `assert elem in it, message`      |
| `lest.assert_not_in(it, elem, message)`  | `assert elem not in it, message`  |
| `lest.assert_raises(err, message)`       | --                                |

`lest.assert_raises` is a context manager.

Example usage of the `lest.assert_raises`:

```python
    # in some test function
    with lest.assert_raises(ZeroDivisionError):
        x = 5 / 0
```

It checks, that given exception raises.
