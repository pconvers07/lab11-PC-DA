"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Input must be a number")


def hypotenuse(a, b):
    # negative numbers are allowed
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Inputs must be numbers")


# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot Divide by Zero")

def logarithm(a, b):
    # log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)


def exponent(a, b):
    return a ** b
