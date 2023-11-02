#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arg[2] != '+' and arg[2] != '-' and arg[2] != '*' and arg[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(arg[1])
    b = int(arg[3])

    if arg[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif arg[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif arg[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif arg[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
