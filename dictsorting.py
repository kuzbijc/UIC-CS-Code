"""
Write a function that takes as argument the dictionary D, as
returned by the function in Problem 20. This function prints out
the elements (key-value pairs) of the dictionary D, sorted according
to the value component, in ascending order.
"""

def f(t): # dictionary
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    t = t.lower()
    #print(t)
    d = {}
    for e in t:
        #print(e)
        if e in al:
            d[e] = t.count(e)
    return d

def g(f): # sorting
    a = f
    b = sorted(a.items(), key = lambda e:e[0])
    for e in b:
        print(e)
  
def main():
    t = "Hello. My name is. My name is. My name is. Slimy Shady."
    g(f(t))
    
main()
