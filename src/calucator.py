"""Module calculatrice simple pour démonstration CI/CD"""

def add(a, b):
    """Additionne deux nombres"""
    return a + b

def subtract(a, b):
    """Soustrait deux nombres"""
    return a - b

def multiply(a, b):
    """Multiplie deux nombres"""
    return a * b

def divide(a, b):
    """Divise deux nombres"""
    if b == 0:
        raise ValueError("Division par zéro impossible!")
    return a / b

def power(a, b):
    """Calcule a puissance b"""
    return a ** b