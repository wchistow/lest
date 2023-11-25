# Using `assert`'s shortcuts

There are some useful functions in the Lest library,
that replaces some common uses of the `assert` keyword:

| lest function                    | assert                                                                                |
|----------------------------------|---------------------------------------------------------------------------------------|
| `lest.assert_eq(first, second)`  | `first` is equal to `second`                                                          |
| `lest.assert_true(exp)`          | `exp` is `True`                                                                       |
| `lest.assert_false(exp)`         | `exp` is `False`                                                                      |
| `lest.assert_in(it, elem)`       | `elem` in `it` iterable object                                                        |
| `lest.assert_not_in(it, elem)`   | `elem` not in `it` iterable object                                                    |
| `lest.assert_raises(err)`        | `err` or its subclass raises with the `message` message (if passed) (context manager) |

Example usage of the `lest.assert_eq`:

```python
    # in some test function
    lest.assert_eq(actual, expected)
```

Examples usage of the `lest.assert_raises`:

1. ```python
       # in some test function
       with lest.assert_raises(ZeroDivisionError):
           x = 5 / 0
   ```
2. ```python
       # in some test function
       with lest.assert_raises(NameError, message="name 'a' is not defined"):
           # will pass, only if the `a` variable does not exist
           x = 5 / 0
   ```
