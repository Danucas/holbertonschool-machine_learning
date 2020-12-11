#!/usr/bin/env python3
"""
Polynomial Derivative from coefficients
"""


def poly_derivative(poly):
    """
    calculates the coefficientes from the derivative
    of poly
    """
    if not isinstance(poly, list) or not all(
            type(n) == int or type(n) == float
            for n in poly) or len(poly) == 1:
        return None
    if len(poly) <= 1:
        return [0]
    coefficients = [
        coeff * (i)
        for i, coeff in
        enumerate(poly[1:], 1)
    ]
    check_all_zeroes = [
        n == 0
        for n in coefficients
    ]
    if all(check_all_zeroes):
        return [0]
    return coefficients[start_index:end_index]
