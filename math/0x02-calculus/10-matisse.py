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
    if len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    checks_ints = [
        type(n) == int or type(n) == float
        for n in poly
    ]
    if not all(checks_ints):
        return None
    coefficients = [
        coeff * (i)
        for i, coeff in
        enumerate(poly)
    ]
    start_index = 0
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            start_index = i
            break
    end_index = len(coefficients)
    for i, coeff in enumerate(reversed(coefficients)):
        if coeff != 0:
            end_index = len(coefficients) - i
            break
    check_all_zeroes = [
        n == 0
        for n in coefficients
    ]
    if all(check_all_zeroes):
        return [0]
    return coefficients[start_index:end_index]
