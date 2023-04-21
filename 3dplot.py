import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np

def main():
    ax = plt.axes(projection = '3d')
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    plt.show()
    
main()
