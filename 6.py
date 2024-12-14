result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первое число меньше второго.")
    if b > 100:
        raise IndexError("Второе число больше 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 15, 8: 4}  # Удалён некорректный ключ []

for key in data:
    try:
        a = int(key)  # Преобразуем ключ к числу, если возможно
        b = data[key]
        res = divider(a, b)
        result.append(res)
    except ZeroDivisionError:
        print(f"Ошибка: Деление на ноль для ключа {key} и значения {data[key]}")
    except ValueError as ve:
        print(f"Ошибка значения: {ve} для ключа {key} и значения {data[key]}")
    except IndexError as ie:
        print(f"Ошибка индекса: {ie} для ключа {key} и значения {data[key]}")
    except TypeError:
        print(f"Ошибка типа: Некорректный тип ключа {key} или значения {data[key]}")

print(result)
