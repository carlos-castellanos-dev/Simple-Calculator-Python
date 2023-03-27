# Assignment 1 Simple Calculator
import math


# Function Definitions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def mod(x, y):
    return x % y


def power(x, y):
    return math.pow(x, y)


def exp(x):
    return math.exp(x)


def log(x):
    return math.log(x)


def absolute(x):
    return abs(x)


# Main
while True:
    print("Simple Calculator")
    print("Please enter x at any point to exit.")
    # First Number Input
    num1 = input("Enter First Number: ")
    try:
        float(num1)
    except ValueError:
        if num1 == 'x':
            print("Exiting")
            break
        else:
            print("Invalid Input")
            break
    num1 = float(num1)
    # Operation Input
    op = input("Enter Operation ['+', '-', '*', '/', '%', '^', 'exp', 'log', 'abs']:")
    if op == 'x':
        break
    elif op == 'log':
        print("log of", num1, "=", log(num1))
    elif op == 'abs':
        print("Absolute Value of", num1, "=", absolute(num1))
    elif op == 'exp':
        print("e to the", num1, "=", exp(num1))
    elif op not in {'+', '-', '*', '/', '%', '^'}:
        print("Invalid Input")
        break
    # Second Number Input
    else:
        num2 = input("Enter Second Number: ")
        try:
            float(num2)
        except ValueError:
            if num2 == 'x':
                print("Exiting")
                break
            else:
                print("Invalid Input")
                break
        num2 = float(num2)
        if op == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif op == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif op == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif op == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif op == '%':
            print(num1, "%", num2, "=", mod(num1, num2))

        elif op == '^':
            print(num1, "^", num2, "=", power(num1, num2))
