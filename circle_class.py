
class circle(object): # class with 3 attributes
    x0 = 1
    y0 = 2
    r = 5

class circle2(object):
    x0 = 1
    y0 = 2
    r = 5
    pi = 3.14

    def circle_area(self):
        return self.pi*(self.r**2)

    def implicit_equation(self):
        return "(x-%i)**2 + (y-%i)**2 = %i" % (self.x0, self.y0, self.r)
        
def main():
    """
    C1 = circle() # instance
    #print(type(C1))
    print(C1.x0)
    print(C1.y0)
    print(C1.r)
    print("-----")
    C2 = circle()
    C2.r = 10
    print(C2.x0)
    print(C2.y0)
    print(C2.r)
    print("-----")
    C3 = circle()
    print(C3.x0)
    print(C3.y0)
    print(C3.r)
    """
    C1 = circle2()
    print(C1.circle_area())
    print(C1.implicit_equation())
    
main()
