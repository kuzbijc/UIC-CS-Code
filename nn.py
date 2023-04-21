
import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return np.exp(x)/(1 + np.exp(x))**2

def main():

    #values
    f_set = np.array([[1,1,1],
                      [1,1,0],
                      [1,0,0],
                      [0,1,1],
                      [0,0,1],
                      [0,1,0],
                      [0,0,0],
                      [1,0,1]])
    #print(f_set)

    predictions = np.array([])
    labels = np.array([[1,1,0,1,0,1,0,0]]).reshape(8,1)
    
    np.random.seed(42)
    weights = np.random.rand(3,1)
    bias = np.random.rand(1)
    lr = 0.05

    #looping; goal: minimize error
    for iterations in range(20000):
        
        #feed forward step1
        XW = np.dot(f_set,weights) + bias
        
        #feed forward step2
        z = sigmoid(XW)
        
        #back propogation step1
        error = z - labels
        #print(error.sum())

        #back propogation part2
        dpred_dz = sigmoid_derivative(z)
        
        zd = error * dpred_dz
        
        inputs = f_set.T
        weights -= lr * np.dot(inputs, zd)

        for num in zd:
            bias -= lr * num
            
    for point in f_set:
        result = sigmoid(np.dot(point,weights)+bias)
        results = np.append(point,result)
        print(results)
    
main()
