# Lest

## Light Python library for testing

## Installing

Just enter in command line:

```shell
pip install lest
```

## Usage

### Example:

Code:

```python
import lest


@lest.register
def test_adding_two_and_two():
    assert 2 + 2 == 4


@lest.register
def some_error_test():
    assert 2 + 2 == 5


lest.run()
```

Output: (To visible the highlighting, run on the command line)

```text
Running [test_adding_two_and_two]... OK
Running [some_error_test]... FAILED:
Traceback (most recent call last):
  File "E:\vladimir\Python\lest\src\lest\runner.py", line 23, in run
    func()
  File "E:\vladimir\Python\lest\src\test.py", line 11, in some_error_test
    assert 2 + 2 == 5
AssertionError

Run 2 tests:
   + Successful: 1
   + Failed: 1
   + Time elapsed: 0.000
```
