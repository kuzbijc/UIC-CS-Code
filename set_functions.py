def main():

    e = set() # empty set

    s = {1, 2, 3, 3, 4, 5, 6} # sets remove duplicates
    s.add(7) # adds 7 to the set
    s.clear() # removes all elements in the set

    a =  {1, 2, 3, 4, 5, 6, 7, 8}
    b = {4, 5, 6, 7, 8, 9, 10, 11}

    d = a.difference(b) # returns what is in a but not in b (a-b)
    #b.discard(11) # discards 11
    e = a.union(b)
    f = a.intersection(b)

    l = {2, 1, 4, 3, 5}
    #print(l.pop()) 

    """
    for pop function:
    if list, grabs/removes last element
    if set, grabs/removes first element
    """
    
    #print(len(l)) # removes duplicates when taking length of set
    #print(sum(l)) # adds non duplicates

    z = sorted(l)
    z = set(z) # converted from list to set
    #print('x' in z) # boolean

    #print({7, 8, 9}.isdisjoint({0, 1, 2, 3, 4})) # boolean, no elements alike "True"
    #print({0, 1, 2, 3, 4}.issuperset({0, 1, 2})) # boolean, first is super of second
    
    print(f)
    
main()
