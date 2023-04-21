
import math

class circle(object):
    pi = math.pi

    def __init__(self,x,y,r):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)

    def __str__(self):
        return "Circle center (%f, %f) and radius %f" % (self.x,self.y,self.r)
    
    def area(self):
        return self.pi*self.r**2

    def area_compare(self,other):
        area1 = self.area()
        area2 = other.area()
        if area1 >= area2:
            return self
        else:
            return other

    def avg_circle(self,other):
        return circle(((self.x + other.x) / 2),((self.y + other.y) / 2),((self.r + other.r) / 2))

    def shift(self,a,b):
        return circle(self.x + a, self.y + b, self.r)
            
def main():
    #c1 = circle(-2,7,5)
    c2 = circle(3,9,10)
    #c3 = circle(0,0,5)
    #c4 = circle(2,2,5)
    #print(c1)
    #print(c1.area())
    #print(c2)
    #c2.pi = 3.14
    #print(c2.area())
    #print(c1.area_compare(c2))
    #print(c1.avg_circle(c2))
    print(c2.shift(17,11))
main()
