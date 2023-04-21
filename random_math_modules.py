
import random
import math

def password_generator(n):
    list_characters = ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
    #password = "".join(random.sample(list_characters, n))
    password = ""
    for i in range(n):
        password += random.choice(list_characters)
    #print(password)
password_generator(4)

# random.sample only works when n <= len(list)
# random.choice will work for any length, regardless of list size

def solve(s):
    l = s.split("*")
    a = int(l[0])
    b = int(l[1].replace("x^2", ""))
    c = int(l[2].replace("x", ""))
    #print(a, b, c)
    descriminant = b**2-4*a*c
    if descriminant > 0:
        print("x0 = %f" % (-b + math.sqrt(descriminant/(2*a))))
        print("x1 = %f" % (-b - math.sqrt(descriminant/(2*a))))
    elif descriminant == 0:
        print("x0 = %f" % (-b/(2*a)))
        print("x1 = %f" % (-b/(2*a)))
    else:
        x = -b/(2*a)
        y = math.sqrt(abs(descriminant)/(2*a))
        print("x0 = %f + %fi" % (x, y))
        print("x0 = %f - %fi" % (x, y))
        
solve("1*x^2-5*x+6")

# first extract the a, b, c (1, -5, 6)
# x0, x1 = (-b +- sqrt(b^2-4*a*c/(2*a))
# if descriminant > 0 then real number roots
# if descriminant == 0 then double root
# if descriminant < 0 then complex root
# for complex numbers, z = x+y*i


