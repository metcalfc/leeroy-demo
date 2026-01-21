"""
Simple calculator module for demonstration purposes.
"""

import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def modulo(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b

def sqrt(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def log(a, base=None):
    """Return the logarithm of a. If base is None, return natural log."""
    if a <= 0:
        raise ValueError("Cannot take logarithm of non-positive number")
    if base is None:
        return math.log(a)
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(a, base)

def sin(a):
    """Return the sine of a (in radians)."""
    return math.sin(a)

def cos(a):
    """Return the cosine of a (in radians)."""
    return math.cos(a)
