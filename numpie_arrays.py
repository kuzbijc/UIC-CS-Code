
import numpy as np # numerical computing with python
import matplotlib.pyplot as plt

def main():
    """
    c = np.array([[11,12,13],[14,15,16]],dtype = float)
    d = np.array([[17,18,19],[20,21,22],[23,24,25]])
    #print(d.shape) # returns dimensions (rows x columns)

    u = np.array([1,2,3])
    v = np.array([4,5,6])
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])

    #print(np.dot(u,v)) # dot product
    #print(np.dot(a,b))
    #print(a.transpose())
    #print(np.linalg.det(b))
    #print(np.linalg.inv(b))
    #print(np.linalg.eig(b))

    a = np.array([1,3,5,6,-1,3,5,6,2])
    print(np.mean(a))
    print(np.median(a))
    print(np.std(a))
    print(np.var(a))

    x = np.array([0,1,2,3,4])
    y = np.array([21,38,59,114,281])
    f = np.polyfit(x,y,4)
    #print(f)
    F = np.poly1d(f) # provides the expression
    #print(F)

    X = np.linspace(-10,10,50)
    Y = F(X)
    plt.plot(x,y,'ro', X,Y,'k-')
    plt.ylim(-100,400)
    plt.legend(['data points','fitted curve'])
    plt.xlabel('x-coor')
    plt.ylabel('y-coor')
    plt.grid()
    plt.show()
    """

    X = np.linspace(-2*np.pi,2*np.pi,100) #(?,?,smoothness)
    Y = np.sin(X)
    plt.plot(X,Y,'g')
    plt.show()

    #plt.scatter([1,2,3,4],[5,6,7,8])
    #plt.grid()
    #plt.show()
    
main()
