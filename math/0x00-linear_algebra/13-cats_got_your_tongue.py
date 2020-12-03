#!/usr/bin/env python3
"""
Concatenates two ndarray at certain index
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    super call to numpy concatenate
    """
    return np.concatenate((mat1, mat2), axis=axis)
