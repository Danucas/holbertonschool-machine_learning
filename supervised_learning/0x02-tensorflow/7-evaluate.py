#!/usr/bin/env python3
"""
Plot accuracy and loss metrics
"""

import tensorflow as tf


def evaluate(X, Y, save_path):
    """
    Load model and evaluate metrics
    """
    sess = tf.Session()
    saver = tf.train.import_meta_graph(save_path + '.meta')
    saver.restore(sess, save_path)
    x = tf.get_collection('x')[0]
    y = tf.get_collection('y')[0]
    y_pred = tf.get_collection('y_pred')[0]
    loss = tf.get_collection('loss')[0]
    accuracy = tf.get_collection('accuracy')[0]

    cost = sess.run(loss, feed_dict={x: X, y: Y})
    acc = sess.run(accuracy, feed_dict={x: X, y: Y})
    pred = sess.run(y_pred, feed_dict={x: X, y: Y})

    return pred, acc, cost
