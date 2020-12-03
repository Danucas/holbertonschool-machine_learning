#!/usr/bin/env python3
"""
Element-wise ndarray operations
"""


def np_elementwise(mat1, mat2):
    """
    tuple returning each operation
    """
    return (
        mat1 + mat2,
        mat1 - mat2,
        mat1 * mat2,
        mat1 / mat2,
    )
