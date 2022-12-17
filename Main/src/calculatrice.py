# calculatrice.py
import math

def add(a, b):
    """Cette fonction retourne la somme de a et b."""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    """Cette fonction retourne la différence de a et b (a - b)."""
    result = a - b
    print(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    """Cette fonction retourne le produit de a et b."""
    result = a * b
    print(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    """Cette fonction retourne le quotient de a et b (a / b).
    Si b vaut 0, une exception ValueError est levée.
    """
    if b == 0:
        raise ValueError("Division par zéro")
    result = a / b
    print(f"{a} / {b} = {result}")
    return result




