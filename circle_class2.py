import math

class circle(object):
    pi = 3.14
    def __init__(self, x, y, r): # initializing your variables
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return "Circle centered at (%f, %f) with radius %f" % (self.x, self.y, self.r)

    def area(self):
        return self.pi*self.r**2

    def larger_area(self, other): # self is c1, other is c2
        a1 = self.area()
        a2 = other.area()
        if a1 > a2:
            return self
        elif a1 < a2:
            return other
        else:
            return "Areas are equal"

    def intersection_exists(self, other):
        #intersect if |r2 - r1| <= sqrt((x2 - x1)**2 + (y2 - y1)**2) <= |r2 + r1|
        s1 = abs(other.r - self.r)
        s2 = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        s3 = abs(other.r + self.r)
        if s1 <= s2 and s2 <= s3:
            return True
        else:
            return False

    def create_average(self, other):
        return circle((self.x + other.x)/2.0, (self.y + other.y)/2.0, (self.r + other.r)/2.0)

    def coordinate_shift(self, a, b):
        # x + a, y + b
        return circle(self.x + a, self.y + b, self.r)
        
def main():
    c1 = circle(0,0, 5)
    c2 = circle(3, 7, 4)
    cs = c1.coordinate_shift(20, 30)
    print(cs)
    #print(c2) # returns address
    #print(c1.__str__())
    #print(c1.area())
    #print(c1.larger_area(c2))
    #print(c1.intersection_exists(c2))
    #print(c1.create_average(c2))
    
main()
