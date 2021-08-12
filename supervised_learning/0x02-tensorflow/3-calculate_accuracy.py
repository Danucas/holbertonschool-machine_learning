#!/usr/bin/env python3
"""
Calculates accuracy
"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    Calculates y pred accuracy
    """
    acc, op = tf.metrics.accuracy(labels=y, predictions=y_pred)
    accuracy = tf.reduce_mean(acc)
    return accuracy
