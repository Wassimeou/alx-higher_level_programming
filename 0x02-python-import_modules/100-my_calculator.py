#!/usr/bin/python3

"""Handle basic arithmetic operations."""
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        result = ops[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    except ValueError:
        print("Error: Both 'a' and 'b' must be integers.")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)
