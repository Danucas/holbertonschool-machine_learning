#!/usr/bin/env python3
"""
Creates Forward propagation graph for the network
"""

import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    Creates layers using layer_sizes and activations
    """
    xN = x
    for size, activation in zip(layer_sizes, activations):
        xN = create_layer(xN, size, activation)
    return xN
