import random

class Cipher:
    def __init__(self, *numbers):
        # Инкапсулированное хранение чисел
        self.__numbers = numbers
        # Вычисление результата при инициализации
        self.__result = self.__process_numbers()

    def __process_numbers(self):
        """Приватный метод, выполняющий случайную математическую операцию."""
        operation = random.choice(['+', '-', '*', '/'])
        result = self.__numbers[0]
        for num in self.__numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/' and num != 0:
                result /= num
        return round(result, 2)  # Округление результата до двух знаков

    def __str__(self):
        """Метод для вывода объекта как строки."""
        return f"Результат вычислений: {self.__result}"

# Пример использования
cipher = Cipher(10, 5, 2)
print(cipher)  # Печатает результат вычислений
