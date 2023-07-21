# Using `assert`'s shortcuts

There are some useful functions in the Lest library,
that replaces some common uses of the `assert` keyword:

| lest function                    | assert                                         |
|----------------------------------|------------------------------------------------|
| `lest.assert_eq(first, second)`  | `first` is equal to `second`                   |
| `lest.assert_true(exp)`          | `exp` is `True`                                |
| `lest.assert_false(exp)`         | `exp` is `False`                               |
| `lest.assert_in(it, elem)`       | `elem` in `it` iterable object                 |
| `lest.assert_not_in(it, elem)`   | `elem` not in `it` iterable object             |
| `lest.assert_raises(err)`        | `err` or its subclass raises (context manager) |

Example usage of the `lest.assert_eq`:

```python
    # in some test function
    lest.assert_eq(actual, expected)
```

Example usage of the `lest.assert_raises`:

```python
    # in some test function
    with lest.assert_raises(ZeroDivisionError):
        x = 5 / 0
```
