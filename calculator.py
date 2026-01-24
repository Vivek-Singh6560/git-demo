import math

def add(a, b):
    """Add two numbers"""
    return a + b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Calculate power"""
    return a ** b


def sqrt(a):
    """Calculate square root"""
    if a < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(a)
