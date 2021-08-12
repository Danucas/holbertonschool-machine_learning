#!/usr/bin/env python3
"""
Calculates accuracy
"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    Calculates y pred accuracy
    """
    accuracy = tf.metrics.accuracy(labels=y, predictions=y_pred)
    return tf.math.reduce_mean(accuracy)
