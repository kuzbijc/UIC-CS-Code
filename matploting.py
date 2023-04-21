
import matplotlib.pyplot as plt
import random

class Coin(object):

    def toss(self):
        v = random.choice([1,-1])
        return v

class Brownian(Coin):
    x = 0
    y = 0
    u = []
    v = []

    def __init__(self,seed,tosses):
        self.seed   = seed
        self.tosses = tosses
        Coin.__init__(self)

    def motion(self):
        self.u.append(self.x)
        self.y = self.seed
        self.v.append(self.y)
        for i in range(1,self.tosses):
            v = self.toss()
            self.x = i
            self.y = self.y + v
            self.u.append(self.x)
            self.v.append(self.y)
        return self.u,self.v

    def plot1(self):
        """
        'b-' = blue solid line
        'ro' = red circles
        'g--'= green dashed line
        'k.' = black dotted line
        """
        plt.plot(self.u,self.v,'ro')
        plt.ylim(min(self.v),max(self.v))
        plt.legend(["Brownian Motion"])
        plt.xlabel("Number of Tosses")
        plt.ylabel("Partial Sums")
        plt.grid()
        plt.show()

def main():
    
    b   = Brownian(0,10) # (seed value,number of tosses)
    u,v = b.motion()
    #print(u)
    #print(v)
    b.plot1()

    
    
main()
