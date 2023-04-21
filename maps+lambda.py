    
def F(x, y):
    return 2*x+10+y

def G(x):
    return x**2

def main():

    M = [0, 1, 2, 3, 4, 5]
    L = [[x,x**2] for x in M] # list of sublists
    #print(L)

    L1 = [[x,x**2] for x in M if x%2 != 0] # for odd numbers only
    #print(L1)

    L2 = [[x,y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y and y % 2 != 0]
    #print(L2)
    
    L3 = [1, 4, 5, 8]
    L4 = [2, 3, 6, 9]
    #for z in map(F, L3, L4):
        #print(z) # mapping accepts 2 arguments

    #print(list(map(pow,[1,2,3,4],[2,2,2,5])))
    # creates a list of a map (comparison to something)
    # and takes the first list to the power of the second

    L = list(map(lambda x: x+10, [1,2,3,4,5,6]))
    #print(L)
     
    h = lambda x: x**2
    #print(h(2))

    A = [[1,27,2],[1,5,6]]
    B = sorted(A, key=lambda x: x[1]) # sorting according to every 2nd element
    C = A.sort(key=lambda x: x[1])
    print(B)
    print(C) # NONE because A is permanently changed, print A when sort is used
    

main()
