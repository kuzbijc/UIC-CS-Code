import math

class point(object):
    """
    a point defined by x,y coordinates
    """
    def __init__(self, x, y): # initialization, only inputs
        self.x = x
        self.y = y

    def point_info(self):
        return "A point (%i, %i)" % (self.x, self.y)

    def distance_origin(self):
        return math.sqrt((self.x - 0)**2 + (self.y - 0)**2)

    def distance_point(self, other): # distance between 2 instances
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class line(object):
    """
    An object line defined by 2 points, P = (Px, Py) and Q = (Qx, Qy)
    """
    def __init__(self, Px, Py, Qx, Qy):
        self.x0 = Px
        self.y0 = Py
        self.x1 = Qx
        self.y1 = Qy

    def line_info(self):
        return "A line segment passing through P = (%i, %i) and Q = (%i, %i)" % (self.x0, self.y0, self.x1, self.y1)

    def slope(self):
        m = (self.y1 - self.y0)/(self.x1- self.x0)
        return m

    def y_int(self):
        m = self.slope()
        b = self.y0 - m*self.x0
        return b

    def parallel(self, other):
        m1 = self.slope()
        m2 = other.slope()
        if m1 == m2:
            return True
        else:
            return False
        
def main():
    L1 = line(1,1, 2,2)
    L2 = line(1,1, 2,2)
    P1 = point(5, 0) # points dont exist in python
    P2 = point(10, 0) 
    #print(P1.point_info())
    #print(P1.distance_origin())
    #print(P2.distance_origin())
    #print(P1.distance_point(P2)) # P1 is self, P2 is other
    #print(L1.line_info())
    #print(L1.slope())
    #print(L1.y_int())
    print(L1.parallel(L2))
     
main()
