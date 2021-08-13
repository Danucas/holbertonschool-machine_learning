#!/usr/bin/env python3
"""
Calculate the loss
"""

import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    Calculates y prediction loss
    """
    return tf.losses.softmax_cross_entropy(y, y_pred)
