import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return np.exp(x) / (1 + np.exp(x))**2

def main():
    x = np.linspace(-10,10,100)
    plt.plot(sigmoid(x), c = 'b')
    plt.plot(sigmoid_derivative(x), c = 'r')
    plt.show()
    
main()
