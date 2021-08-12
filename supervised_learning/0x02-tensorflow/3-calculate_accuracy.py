#!/usr/bin/env python3
"""
Calculates accuracy
"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    Calculates y pred accuracy
    """
    pred_check = tf.equal(y_pred, y)
    acc_op = tf.reduce_mean(tf.cast(pred_check, tf.float32))
    return acc_op
