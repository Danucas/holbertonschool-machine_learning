#!/usr/bin/env python3
"""
Run a train routine
"""

import tensorflow as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(
        X_train, Y_train, X_valid,
        Y_valid, layer_sizes, activations,
        alpha, iterations, save_path="/tmp/model.ckpt"):
    """
    Train running, Shoo Shoo !!
    """
    x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
    y_pred = forward_prop(x, layer_sizes, activations)
    accuracy = calculate_accuracy(y, y_pred)
    loss = calculate_loss(y, y_pred)
    train_op = create_train_op(loss, alpha)
    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('y_pred', y_pred)
    tf.add_to_collection('loss', loss)
    tf.add_to_collection('accuracy', accuracy)
    tf.add_to_collection('train_op', train_op)

    init = tf.global_variables_initializer()

    training_dict = {
        x: X_train,
        y: Y_train
    }

    validation_dict = {
        x: X_valid,
        y: Y_valid
    }

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(init)
        for i in range(iterations + 1):
            t_loss, t_acc = sess.run(
                (loss, accuracy), feed_dict=training_dict)
            val_loss, val_acc = sess.run(
                (loss, accuracy), feed_dict=validation_dict)
            if i % 100 == 0 or i == iterations:
                print_results(
                    i,
                    t_loss,
                    t_acc,
                    val_loss,
                    val_acc)
            if i < iterations:
                sess.run(train_op, feed_dict=training_dict)
        return saver.save(sess, save_path)


def print_results(iteration, t_loss, t_acc, val_loss, val_acc):
    """
    Prints results
    """
    message = ("After {iteration} iterations:\n"
               "\tTraining Cost: {cost}\n"
               "\tTraining Accuracy: {accuracy}\n"
               "\tValidation Cost: {val_cost}\n"
               "\tValidation Accuracy: {val_acc}"
               )
    print(message.format(
        iteration=iteration,
        cost=t_loss,
        accuracy=t_acc,
        val_cost=val_loss,
        val_acc=val_acc
    ))
