import math
class vector(object):
    def __init__(self, x, y, z):
        self.x = 1.0*x # converted to float
        self.y = 1.0*y
        self.z = 1.0*z

    def __str__(self): # overloading string function
        return "<%f, %f, %f>" % (self.x, self.y, self.z) # floating point

    def __add__(self, other): # overloading add function
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rmul__(self, constant):
        return vector(constant*self.x, constant*self.y, constant*self.z)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def norm(self): # value used to rescale vector to magnitude 1
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def unit(self): # normalization, or returns vector with length 1
        n = self.norm()
        return vector(self.x/n, self.y/n, self.z/n)

    def cross(self, other): # cross product
        return vector(self.y*other.z - self.z*other.y, -1*(self.x*other.z - self.z*other.x), self.x*other.y - self.y*other.x)

def main():
    v1 = vector(1, -5, 10) # instance
    v2 = vector(3, 2, 7) # instance
    print(v1 + v2) # returns added coordinates in vector form
    print(v1 - v2) # returns subtracted coordinates in vector form
    print(4*v1) # returns vector multiplied by constant
    print(v1.dot(v2))
    n = v1.norm()
    print(n)
    u = v1.unit()
    print(u)
    c = v1.cross(v2)
    print(c)
    
main()
