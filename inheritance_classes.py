
import math
class A(object):

    def __init__(self, x):
        self.x = x

    def square(self):
        return self.x**2

class B(object):

    def __init__(self, y):
        self.y = y

    def sroot(self):
        return math.sqrt(self.y)

class C(A, B):

    def __init__(self, z):
        self.z = z
        A.__init__(self, z)
        B.__init__(self, z)

    def summation(self):
        return self.square() + self.sroot()

    def double(self):
        return 2 * self.z

class A2(object):

    def __init__(self, s):
        self.s = s

    def num_char(self):
        return len(self.s)

class A3(object):

    def __init__(self, s):
        self.s = s

    def num_words(self):
        return self.s.count(" ") + 1

class A4(A2, A3):

    def __init__(self, s):
        self.s = s
        A2.__init__(self, s)
        A3.__init__(self, s)

    def num_words_letters(self):
        return (self.num_char(), self.num_words())

    def cap_letters(self):
        s = 0
        for e in self.s:
            if e != e.lower(): #e.upper() does not ignore spaces
                s += 1
        return s
        
def main():
    s = "Programming with Python is super easy"
    a = A(5)
    b = B(5)
    c = C(5)
    d = A2(s)
    e = A3(s)
    f = A4(s)
    print(f.num_words_letters())
    
main()
