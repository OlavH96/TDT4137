import math
import numpy as np
import random
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def mse(x, y):
    return math.sqrt((y - x) ** 2)


def activate(row, weights, theta=0.5):

    sum = 0
    for i in range(len(row)):
        sum += weights[i] * row[i]
    return 1.0 if sum >= theta else 0.0


def train_weights(error, weights, learning_rate):

    for i in range(len(weights)):
        weights[i] = weights[i] + learning_rate * error



    w0_history.append(weights[0])
    w1_history.append(weights[1])


if __name__ == '__main__':
    steps = 100
    learning_rate = 0.01
    theta = 1

    number_of_neurons = 2
    random_range = [-0.5, 0.5]

    # inputs = [[1, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0]]  # AND input
    inputs = [[1, 1, 1], [0, 0, 0], [1, 0, 1], [0, 1, 1]]  # OR input

    weights = [random.uniform(*random_range) for i in range(number_of_neurons)]

    errors = []
    w0_history = [weights[0]]
    w1_history = [weights[1]]

    for step in range(steps):
        print("Step", step)
        print("Weights", weights)

        random.shuffle(inputs)

        for i in range(len(inputs)):
            input = inputs[i][:-1]

            # Multiply input by weights and use activation function
            output = activate(input, weights, theta)
            exp_output = inputs[i][-1]

            error = mse(output, exp_output)
            errors.append(error)

            train_weights(error, weights, learning_rate)
            print("Prediction", output, "Actual", exp_output, "Error", error)

    plt.plot(errors)
    plt.show()

    plt.plot(w0_history)
    plt.plot(w1_history)
    plt.title("OR Weights history")
    plt.legend(["Weight 0", "Weight 1"])
    plt.show()
