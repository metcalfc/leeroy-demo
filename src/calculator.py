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
