#!/usr/bin/env python3
"""
Polynomial Derivative from coefficients
"""


def poly_derivative(poly):
    """
    calculates the coefficientes from the derivative
    of poly
    """
    if type(poly) != list:
        return None
    checks_ints = [
        type(n) == int
        for n in poly
    ]
    if not all(checks_ints):
        return None
    coefficients = [
        coeff * (i)
        for i, coeff in
        enumerate(poly)
    ]
    # Forwards
    indexes = []
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            break
        indexes.append(i)
    for index in indexes:
        del coefficients[index]
    # Backwards
    coefficients.reverse()
    indexes = []
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            break
        indexes.append(i)
    for index in indexes:
        del coefficients[index]
    coefficients.reverse()
    return coefficients
