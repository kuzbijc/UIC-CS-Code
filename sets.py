



def main():

    s = set() # {} without elements is dictionary
    s = {1,2,3,4,5,6}
    #print(type(s))
    s.add("hello") # adds to end of set
    s.clear() # obviously clears the set idiot
    #print(s)

    a = {1,2,3,4,5,6,7,8,9}
    b = {1,2,3,10,11,12}
    d = a.difference(b) # comparing differences of a to b
    print(d)
    d.discard(3) # removes elements
    #d.remove(7) # also removes element
    #print(a.union(b))
    #print(a.intersection(b))
    #print(a.isdisjoint(b))
    #print(a.issubset(b))
    #print(a.issuperset(b))
    #print(a.pop())
    #print(a.symmetric_difference(b)) # stronger difference comparison
    x = {1,3,5,7,6,5,3}
    #print(sorted(x)) # permanent sort
    for e in x:
        print(e/2)
    
    
    
main()
