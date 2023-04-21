import math

class vector(object):

    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "<%f,%f,%f>" % (self.x,self.y,self.z)

    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y,self.z-other.z)

    def __rmul__(self,c): # our type is on the right side (5*u)
        return vector(c*self.x,c*self.y,c*self.z)

    def dot_product(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def norm(self): # magnitude(length) of vector
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def normalize(self):
        norm = self.norm()
        return vector(self.x/norm,self.y/norm,self.z/norm)

    def cross(self,other):
        return vector(self.y*other.z-self.z*other.y,-(self.x*other.z-self.z*other.x),self.x*other.y-self.y*other.x)
 

def main():
    u = vector(1,2,3)
    v = vector(4,-5,1)
    #print(u)
    #print(v)
    #print(u+v)
    #print(u-v)
    #print(5*u)
    #print(u.dot_product(v))
    #print(u.norm())
    #print(u.normalize())
    #print(u.cross(v))
    

main()
