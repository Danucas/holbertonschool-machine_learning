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
    g = tf.Graph()
    with g.as_default():
        x, y = create_placeholders(X_train.shape[1], Y_train.shape[1])
        y_pred = forward_prop(x, layer_sizes, activations)
        accuracy = calculate_accuracy(y, y_pred)
        loss = calculate_loss(y, y_pred)
        train_op = create_train_op(loss, alpha)
        tf.add_to_collection('placeholders', x)
        tf.add_to_collection('placeholders', y)
        tf.add_to_collection('tensors', y_pred)
        tf.add_to_collection('tensors', loss)
        tf.add_to_collection('tensors', accuracy)
        tf.add_to_collection('operation', train_op)

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
        config = tf.ConfigProto(
            intra_op_parallelism_threads=0,
            inter_op_parallelism_threads=2,
            allow_soft_placement=True)
        with tf.Session(config=config) as sess:
            sess.run(init)
            batch_size = len(X_train) // iterations
            start = 0
            for i in range(iterations + 1):
                # Get 0th iteration
                if i == 0:
                    # Compute loss and accuracy for training
                    t_loss, t_acc = sess.run(
                        (loss, accuracy), feed_dict={
                            x: X_train[start:start + batch_size],
                            y: Y_train[start:start + batch_size]
                        })
                else:
                    _, t_loss, t_acc = sess.run(
                        (train_op, loss, accuracy), feed_dict={
                            x: X_train[start:start + batch_size],
                            y: Y_train[start:start + batch_size]
                        })
                    start = start + batch_size

                # Validate each 100 iterations
                if i % 100 == 0 or i == iterations:
                    # Compute loss and accuracy for validation
                    val_loss, val_acc = sess.run(
                        (loss, accuracy), feed_dict=validation_dict)

                    # Print all losses and accuracies
                    print_results(i, t_loss, t_acc, val_loss, val_acc)

            saver.save(sess, save_path)
    return save_path


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
