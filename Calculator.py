# from decimal import Decimal
# from fractions import Fraction

import re


class Caalculator:
    def __init__(self) -> None:
        pass

    # Метод класса используется для вычисления значений с заданной точностью.
    @classmethod
    def precise_calculator(cls, x1, x2):
        # Определяем кол-во знаков после запятой для обоих операндов
        x1_decimal_places = len(str(x1).split(".")[1]) if "." in str(x1) else 0
        x2_decimal_places = len(str(x2).split(".")[1]) if "." in str(x2) else 0

        # Находим максимальное кол-во знаков после запятой
        max_decimal_places = max(x1_decimal_places, x2_decimal_places)

        # Вычисляем множитель, который необходимо использовать для привидения чисел к целому типу
        cls.multiplier = 10**max_decimal_places
        # Приводим оба числа к целому типу с учетом количества знаков после запятой
        cls.int_x1 = int(x1 * cls.multiplier)
        cls.int_x2 = int(x2 * cls.multiplier)

    # Методы, возвращающие результат арифметических операций над числами
    def add(self, x1, x2) -> float:
        return float((self.int_x1 + self.int_x2) / self.multiplier)

    def subtract(self, x1, x2) -> float:
        return float((self.int_x1 - self.int_x2) / self.multiplier)

    def multiply(self, x1, x2) -> float:
        return float((self.int_x1 * self.int_x2) / self.multiplier)

    def divide(self, x1, x2) -> float:
        return (
            float((self.int_x1 / self.int_x2) / self.multiplier)
            if x2 != 0
            else "zero error"
        )

    def readline(self, line) -> dict:
        print("===Reading line started...===")

        # Инициализируем словарь для хранения компонентов арифметического выражения и его результата
        splited_line = {"a": "???", "b": "???", "f": "???", "r": "???"}

        # Компилируем регулярное выражение для поиска арифметического выражения в строке
        pattern = re.compile(
            r"([0-9.]+)\s*([+\-*/])\s*([0-9.]+)"
        )  # Паттерн для поиска выражения

        # Ищем соответствие регулярному выражению в строке
        match = pattern.match(line)
        if match:
            # Если соответствие найдено, извлекаем компоненты выражения
            splited_line["a"] = match.group(1)
            splited_line["f"] = match.group(2)
            splited_line["b"] = match.group(3)

            operand1 = float(splited_line["a"])
            operand2 = float(splited_line["b"])

            # Выполняем точные вычисления для операндов
            self.precise_calculator(operand1, operand2)

            # Выполняем соответствующую операцию в зависимости от знака операции
            if splited_line["f"] == "+":
                splited_line["r"] = self.add(operand1, operand2)
            elif splited_line["f"] == "-":
                splited_line["r"] = self.subtract(operand1, operand2)
            elif splited_line["f"] == "*":
                splited_line["r"] = self.multiply(operand1, operand2)
            elif splited_line["f"] == "/":
                splited_line["r"] = self.divide(operand1, operand2)

        # Выводим информацию о прочитанном выражении и его результате
        print("===Reading line finished...===")
        print(
            splited_line["a"],
            " ",
            splited_line["f"],
            " ",
            splited_line["b"],
            " = ",
            splited_line["r"],
        )

        return splited_line


# calculator = Caalculator()

# line = Caalculator.readline(Caalculator, "1+1+1")
# operand1 = float(line["a"])
# operand2 = float(line["b"])
# Caalculator.precise_calculator(operand1, operand2)
