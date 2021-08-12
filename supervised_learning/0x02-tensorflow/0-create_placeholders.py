#!/usr/bin/env python3
"""
Creates placeholders with Tensorflow
"""

import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Defines the inputs to the neural network
    and the one-hot labels for the input data
    """
    x = tf.placeholder(tf.float32, [None, nx])
    y = tf.placeholder(tf.float32, [None, classes])
    return (
        tf.identity(x, name="x"),
        tf.identity(y, name="y")
    )
