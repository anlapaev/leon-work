import math
from Calculator import Caalculator as Calc

def eventer(event, values) -> dict:
    line = {"a": "", "b": "", "f": "", "r": ""}
    calc = Calc() 
    line = calc.readline(values["-IN-"])
    operand1 = float(line["a"])
    operand2 = float(line["b"])
    calc.precise_calculator(operand1, operand2)

    if line["f"] == "+":
        line["r"] = calc.add(operand1, operand2)
        print(line["r"])

    if line["f"] == "-":
        line["r"] = calc.subtract(operand1, operand2)
        print(line["r"])

    if line["f"] == "*":
        line["r"] = calc.multiply(operand1, operand2)
        print(line["r"])

    if line["f"] == "/":
        line["r"] = calc.divide(operand1, operand2)
        print(line["r"])

    return line
