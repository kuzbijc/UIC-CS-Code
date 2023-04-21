import tensorflow as tf
import random
import numpy as np

class neural_network(object):
    def __init__(self,x,y):
        self.input = x
        self.y = y
        self.weights1 = np.random.rand(self.input.shape[1],2) # <-------- 
        self.weights2 = np.random.rand(1,1)
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = tf.nn.sigmoid(np.dot(self.input, self.weights1))
        self.output = tf.nn.sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

def main():
    a = np.array()
    b = np.array()
    A = neural_network()
    print(A.backprop())

main()
