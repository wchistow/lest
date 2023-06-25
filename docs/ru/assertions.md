# Использование сокращений для ключевого слова `assert`


В библиотеке Lest есть несколько полезных функций,
которые заменяют некоторые часто встречающиеся использования ключевого слова `assert`:

| функция из библиотеки Lest               | аналагичный `assert`              |
|------------------------------------------|-----------------------------------|
| `lest.assert_eq(first, second, message)` | `assert first == second, message` |
| `lest.assert_true(exp, message)`         | `assert exp, message`             |
| `lest.assert_false(exp, message)`        | `assert not exp, message`         |
| `lest.assert_in(it, elem, message)`      | `assert elem in it, message`      |
| `lest.assert_not_in(it, elem, message)`  | `assert elem not in it, message`  |
| `lest.assert_raises(err, message)`       | --                                |

`lest.assert_raises` - контекстный менеджер.

Пример использования `lest.assert_raises`:

```python
    # в тесте
    with lest.assert_raises(ZeroDivisionError):
        x = 5 / 0
```

Он проверяет, что переданное исключение вызывается.
