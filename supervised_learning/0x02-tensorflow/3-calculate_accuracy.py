#!/usr/bin/env python3
"""
Calculates accuracy
"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    Calculates y pred accuracy
    """
    corrected_pred = tf.equal(
        tf.argmax(y_pred, 1),
        tf.argmax(y, 1)
    )
    accuracy = tf.reduce_mean(tf.cast(corrected_pred, tf.float32))
    return accuracy
