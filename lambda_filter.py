
def avg(l1, l2):
    avg1 = (l1 + l2) / 2
    return avg1


def f(l):
    for e in l1:
        if e == 5:
            print(e)


def f(l4):
                
    l = []
    for e in l4:
        #print(e)
        if '5' in str(e):
            l.append(e)
        return l
    
    
def f1(l5):
    for e in l5:
        #print(e)
        if e > 0:
            #print(e)
            e1 = e % 4
    return e1
            

def main():

    
    #l1 = [1, 2, 3]
    #l2 = [2, 4, 6]
    #l3 = list(map(avg, l1, l2)) # creates list of averages through mapping
    l4 = [5, 10, 15, 16, 17, 20]
    #print(f(l4)) # not working
    #print(list(filter(lambda x: '5' in str(x) and x % 5 == 0, l4))) # not working

    l5 = [-2, -4, 2, 4, 6, 8]
    #print(f1(l5)) # not working

    #print([x % 4 for x in l5 if x > 0]) # makes list of positive int remainders
    b = [[1, 3, 2], [1, 2, 3], [7, 1, 3]]
    a = sorted(b, key = lambda x: x[2]) # not working
    #print(a

    l = [1, 2, 3, 4, 5]
    print("".join([str(x) for x in l if x % 2 != 0])) # changes list of numbers to a string of numbers


main()
