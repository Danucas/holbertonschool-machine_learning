#!/usr/bin/env python3
"""
Calculates accuracy
"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    Calculates y pred accuracy
    """
    accuracy = tf.contrib.metrics.accuracy(
        tf.cast(y_pred, dtype=tf.bool),
        tf.cast(y, dtype=tf.bool)
    )
    return accuracy
