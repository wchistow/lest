# Использование сокращений для ключевого слова `assert`

В библиотеке Lest есть несколько полезных функций,
которые заменяют некоторые часто встречающиеся использования ключевого слова `assert`:

| функция из библиотеки Lest           | утверждение                                                                                              |
|--------------------------------------|----------------------------------------------------------------------------------------------------------|
| `lest.assert_eq(first, second)`      | `first` равно `second`                                                                                   |
| `lest.assert_true(exp)`              | `exp` - это `True`                                                                                       |
| `lest.assert_false(exp)`             | `exp` - это `False`                                                                                      |
| `lest.assert_in(it, elem)`           | `elem` содержится в итерируемом объекте `it`                                                             |
| `lest.assert_not_in(it, elem)`       | `elem` не содержится в итерируемом объекте `it`                                                          |
| `lest.assert_raises(err[, message])` | возникает исключение `err` или её подкласс с сообщением `message` (если передано) (контекстный менеджер) |

Пример использования `lest.assert_raises`:

```python
    # в тесте
    lest.assert_eq(actual, expected)
```

Примеры использования `lest.assert_raises`:

1. ```python
       # в тесте
       with lest.assert_raises(ZeroDivisionError):
           x = 5 / 0
   ```
2. ```python
       # в тесте
       with lest.assert_raises(NameError, message="name 'a' is not defined"):
           # пройдёт, только если не существует переменная `a`
           print(a, b)
   ```
