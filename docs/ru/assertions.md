# Использование сокращений для ключевого слова `assert`

В библиотеке Lest есть несколько полезных функций,
которые заменяют некоторые часто встречающиеся использования ключевого слова `assert`:

| функция из библиотеки Lest      | утверждение                                                       |
|---------------------------------|-------------------------------------------------------------------|
| `lest.assert_eq(first, second)` | `first` равно `second`                                            |
| `lest.assert_true(exp)`         | `exp` - это `True`                                                |
| `lest.assert_false(exp)`        | `exp` - это `False`                                               |
| `lest.assert_in(it, elem)`      | `elem` содержится в итерируемом объекте `it`                      |
| `lest.assert_not_in(it, elem)`  | `elem` не содержится в итерируемом объекте `it`                   |
| `lest.assert_raises(err)`       | возникает исключение `err` или её подкласс (контекстный менеджер) |

Пример использования `lest.assert_raises`:

```python
    # в тесте
    lest.assert_eq(actual, expected)
```

Пример использования `lest.assert_raises`:

```python
    # в тесте
    with lest.assert_raises(ZeroDivisionError):
        x = 5 / 0
```
