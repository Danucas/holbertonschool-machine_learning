#!/usr/bin/env python3
"""
Creates a Layer with Tensorflow
"""

import tensorflow as tf


def create_layer(prev, n, activation):
    """
    defines a layer with activation He et. al
    """
    initializer = tf.contrib.layers.variance_scaling_initializer(
        mode="FAN_AVG",
        dtype=tf.dtypes.float32
    )

    layer = tf.layers.Dense(
        n,
        activation=activation,
        name="layer",
        kernel_initializer=initializer
    )

    return layer(prev)
