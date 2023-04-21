l
def f(x):
    return 2*x
        
def main():

    l1 = [x**2 for x in range(10)] # list comprehension
    #print(l1)

    l2 = [z+2*z for z in [1, 3, 5, -4, 20]]
    #print(l2)

    m = ['a', 'X', 3.1, 7, 8, '9', [1, 2, 3], (5, 6, 13), 10]
    l3a = [x**2 for x in m if type(x) == int]
    #print(l3a)

    l3b = [x**2 for x in m if type(x) == float or type(x) == int]
    #print(l3b)

    l4 = [1, 4, 5, 8]
    l5 = [2, 3, 6, 9]

    #for z in map(min, l4, l5): # compares lists
        #print(z)
    
    #print(pow(2, 4)) # 2 to the power of 4

    #print(list(map(pow, [1, 2, 3, 4, 5], [2, 2, 2, 2, 2]))) # number of arguments depends on the function inside of map

    #print(f(10)) # same as g

    g = lambda x: 2*x # lambda is a function without a name
    #print(g(10))

    l6 = [lambda x: x, lambda x: x**2, lambda x: x**3]
    #for e in l:
        #print(e(2))
    l6 = list(map(lambda x: x + 10, [1, 2, 3, 4, 5]))
    #print(l6)

    l7 = list(filter(lambda x: x > 0, [-5, 3, -3, 7, 0, 1, 9])) # filters out the negatives
    #print(l7)

    a = [[1, 7, 5], [4, 9, 8], [3, 1, 2], [9, 2, 6]]
    b = sorted(a, key = lambda x: x[2]) # sorting elements based off 2nd index in elements
    print(b)    


main()
