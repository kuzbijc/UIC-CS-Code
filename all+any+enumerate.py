
def main():
    L = [0, 1, 2, 3, 4, 5, 6]
    #print(L[::-3]) # negative reverses the list, so -3 means
                   # to skip 3 steps backwards
    #print(L+L) # creates a new list of L elements twice

    print(all([False, False, False, False]))# returns false
    print(all([0,1,2,3,4])) # returns false, 0 is false
    print(all([1,2,3,4])) # returns true, 1 is true
    print(any([False, True, False, False])) # returns True
    # all is like AND
    # any is like OR

    print(list(enumerate(['a','b','c','d','e']))) # returns tuple with index
    print(list(enumerate("hello"))) # splices the text, tuples with index  

main()
