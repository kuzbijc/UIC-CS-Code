
def f(): # for 3 variables, how about x number of variables?
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x = bool(i)
                y = bool(j)
                z = bool(k)
                print((x and not y) or (x and z))

def truth(n):
    for i in range(2**n):
        s = bin(i).split("0b")[1]
        print((n-len(s))*"0"+s, "=", i) # prints binary of the numbers
 
def main():
    f()
    #truth(5)
    
main()
