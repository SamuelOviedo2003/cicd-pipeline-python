"""
This module provides functions to calculate
"""

# app/calculadora.py

AUTORES = "Samuel Oviedo Paz"


def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b


def restar(a, b):
    """Resta dos números y retorna el resultado."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números y retorna el resultado."""
    return a * b


def dividir(a, b):
    """Divide dos números y retorna el resultado."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
