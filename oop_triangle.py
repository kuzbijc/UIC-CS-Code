
import math
class triangle(object):

    def __init__(self,ax,ay,bx,by,cx,cy):
        self.ax = 1.0*ax
        self.ay = 1.0*ay
        self.bx = 1.0*bx
        self.by = 1.0*by
        self.cx = 1.0*cx
        self.cy = 1.0*cy
        self.AB = abs(math.sqrt((self.ax-self.bx)**2 + (self.ay-self.by)**2))
        self.AC = abs(math.sqrt((self.ax-self.cx)**2 + (self.ay-self.cy)**2))
        self.CB = abs(math.sqrt((self.cx-self.bx)**2 + (self.cy-self.by)**2))
    
    def __str__(self):
        return "Triangle((%f,%f),(%f,%f),(%f,%f))" % (self.ax, self.ay, self.bx, self.by, self.cx, self.cy)

    def area(self): #herons formula
        S = (self.AB + self.AC + self.CB) / 2 # semi-perimeter, half the perimeter
        area = math.sqrt(S*((S-self.AB)*(S-self.AC)*(S-self.CB)))
        return "Area: %f" % area

    def perimeter(self):
        perimeter = self.AB + self.AC + self.CB
        return "Perimeter: %f" % perimeter

    def barycenter(self):
        centerx = (self.ax + self.bx + self.cx) / 3
        centery = (self.ay + self.by + self.cy) / 3
        return "Barycenter: (%f, %f)" % (centerx, centery)
    
    def longestside(self):
        longest = max(self.AB, self.AC, self.CB)
        return "Longest side: %f" % longest

    def isrighttriangle(self):
        e = 0.00000001 # 10**-8
        if abs(self.AB**2 + self.AC**2 - self.CB**2) < e:
            return "Right triangle: True"
        elif abs(self.AB**2 + self.CB**2 - self.AC**2) < e:
            return "Right triangle: True"
        elif abs(self.AC**2 + self.CB**2 - self.AB**2) < e:
            return "Right triangle: True"
        else:
            return "Right triangle: False"
    
def main():
    
    t1 = triangle(3, -5,  15, 4,  -6, 10)
    print(t1)
    print(t1.area())
    print(t1.perimeter())
    print(t1.barycenter())
    print(t1.longestside())
    print(t1.isrighttriangle())

main()

"""
OUTPUT:
Triangle((3.000000,-5.000000),(15.000000,4.000000),(-6.000000,10.000000))
Area: 130.500000
Perimeter: 54.333185
Barycenter: (4.000000, 3.000000)
Longest side: 21.840330
Right triangle: False
"""
