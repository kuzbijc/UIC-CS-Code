import math

class rectangle(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w*self.h

    def perimeter(self):
        return 2*self.w + 2*self.h

class square(rectangle):

    def __init__(self, z):
        self.z = z
        rectangle.__init__(self, z, z)

class vector(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "<%f, %f>" % (self.x, self.y)

    def magnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def quadrant(self):
        a = self.x
        b = self.y
        if a >= 0 and b >= 0:
            return "Vector in quadrant 1"
        elif a < 0 and b >= 0:
            return "Vector in quadrant 2"
        elif a >= 0 and b < 0:
            return "Vector in quadrant 3"
        else:
            return "Vector in quadrant 4"

class complex(vector):

    def __init__(self, x, y):
        self.x = 1.0*x
        self.y = 1.0*y
        vector.__init__(self, x, y)

    def __str__(self):
        if self.y >= 0:
            return "z = %f + %fi" % (self.x, self.y)
        else:
            return "z = %f - %fi" % (self.x, -abs(self.y))

    def __mul__(self, z):
        return complex(self.x*z.x - self.y*z.y, self.x*z.y + self.y*z.x)
 
def main():
    r = rectangle(1, 4) # w, h
    ra = r.area()
    rp = r.perimeter()
    s = square(3)
    sa = s.area()
    sp = s.perimeter()

    v = vector(7, 9)
    c = complex(2, 5)
    z = complex(1, 6)

    print(z.__mul__(c))
    
main()
