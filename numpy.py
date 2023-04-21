
import numpy as np
import matplotlib.pyplot as plt

def main():
    A = np.array([1, 2, 3, 4])
    B = np.array((4, 5, 6, 7))
    C = np.array([(1, 2, 3, 4), (5, 6, 7, 8)], dtype = float) # 2D array
    D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # matrix
    #print(D, type(D))

    u = np.array([1, 2, 3])
    v = np.array([1, 1, 1])
    #print(np.dot(u, v))

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    #print(np.dot(a, b))
    #print(a)
    #print(np.transpose(a))
    #print(np.linalg.det(a))
    #print(np.linalg.inv(a))
    #print(np.linalg.eig(a)) # eigen vectors with eigen values

    h = np.array([1, 2, 1, 2, 3, 2, 37, 4, 3, 4, 5, 4])
    #print(np.mean(h))
    #print(np.median(h))
    #print(np.std(h)) # standard deviation, deviating from mean value
    #print(np.var(h)) # std**2 how spread out data is

    x = np.array([0, 1, 2, 3, 4])
    y = np.array([21, 38, 59, 114, 281])
    f = np.polyfit(x, y, 2) # x, y, degree polynomial
    #print(f) # coefficients
    F = np.poly1d(f)
    print(F) # actual function

    X = np.linspace(-10, 10, 50) # HIGHER NUMBER = SMOOTHER GRAPH
    Y = F(X)
    plt.plot(x, y, 'ro', X, Y, 'k')
    plt.legend('data points', 'fitted cuve')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.grid()
    plt.show()

    plt.scatter(x, y)
    plt.grid()
    plt.show()

main()
