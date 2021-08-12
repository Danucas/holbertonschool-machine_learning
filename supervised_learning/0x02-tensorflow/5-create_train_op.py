#!/usr/bin/env python3
"""
Creates the Training routine
"""

import tensorflow as tf


def create_train_op(loss, alpha):
    """
    Creates the steps for a training session
    """
    optimizer = tf.train.GradientDescentOptimizer(alpha)
    train = optimizer.minimize(loss)
    return train
