
class matrix(object):

    def __init__(self,l):
        self.a = float(l[0][0])
        self.b = float(l[0][1])
        self.c = float(l[1][0])
        self.d = float(l[1][1])
        
    def __str__(self):
        return "[%f,%f]\n[%f,%f]" % (self.a,self.b,self.c,self.d)

    def determinant(self):
        return (self.a*self.d) - (self.b*self.c)

    def trace(self):
        return self.a + self.d

    def inverse(self):
        det = self.determinant()
        if det != 0:
            oo = self.d/det
            ot = -(self.b)/det
            to = -(self.c)/det
            tt = self.a/det
            return "[%f,%f]\n[%f,%f]" % (oo,ot,to,tt)
        else:
            return "Matrix singular/not invertible."

    def char(self):
        det = self.determinant()
        tra = self.trace()
        v = 0.00000000001
        if tra > v and det > v:
            return "x^2-%f*x+%f" % (tra,det)
        elif tra > v and det < v:
            return "x^2-%f*x-%f" % (tra,abs(det))
        elif tra < v and det > v:
            return "x^2+%f*x+%f" % (abs(tra),det)
        elif tra < v and det < v:
            return "x^2+%f*x-%f" % (abs(tra),abs(det))

    def prod(self,other):
        oo = (self.a*other.a)+(self.b*other.c)
        ot = (self.a*other.b)+(self.b*other.d)
        to = (self.c*other.a)+(self.d*other.c)
        tt = (self.c*other.b)+(self.d*other.d)
        return "[%f,%f]\n[%f,%f]" % (oo,ot,to,tt)
    
def main():
    a = matrix([[1,2],[3,4]])
    b = matrix([[5,6],[7,8]])
    print("PROJECT 1")
    print("-----------------------------")
    print("ORIGINAL MATRIX:")
    print(a)
    print("DETERMINANT:")
    print(a.determinant())
    print("TRACE:")
    print(a.trace())
    print("INVERSE MATRIX:")
    print(a.inverse())
    print("CHARACTERISTIC FUNCTION:")
    print(a.char())
    print("PRODUCT MATRIX:")
    print(a.prod(b))

main()
