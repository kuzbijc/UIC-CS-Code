#plotting
import matplotlib.pyplot as plt
import random

class coin(object):

    def flip():
        r = random.choice([-1,1])
        return r
        
class brownian(coin):
    x = 0
    y = 0
    U = [] # x axis
    V = [] # y axis
    R = [] # rolls (-1 or 1)

    def __init__(self, seed_value, coin_flips):
        self.seed = seed_value
        self.flip = coin_flips
        coin.__init__(self)
        
    def motion(self):
        self.y = self.seed
        self.U.append(self.x)
        self.V.append(self.y)
        for i in range(1, self.flip):
            r = self.flip()
            self.x = i
            self.y = self.y + r
            self.R.append(r)
            self.U.append(self.x)
            self.V.append(self.y)
        return self.U, self.R, self.V

    def plot(self):
        """
        b-  = blue solid line
        ro  = red circles
        g-- = green dashed line
        k.  = black dotted line
        """
        plt.plot(self.U, self.V, 'b-')
        plt.ylim(min(self.V), max(self. V))
        plt.legend("Brownian Motion")
        plt.xlabel("Number of Coin Flips")
        plt.ylabel("Change from Seed Value")
        plt.grid()
        plt.show()

def main():
    B = brownian(0,10) # 0 is starting point, 100 is number of coin tosses
    U, V, R = B.motion()
    print(U)
    print(V)
    print(R)
    print(B.plot())

main()
