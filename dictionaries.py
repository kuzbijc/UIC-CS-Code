


def main():

    d = {'a':1,'b':2,'c':3} # or d = dict()
    print(d.items())
    print(d.keys(),d.values())
    d['d'] = 4 # or d.update({'d':4})
    print(d)

    l = ['a','b','c']
    d2 = {}.fromkeys(l) # creates dictionary without values
    d3 = {}.fromkeys(l,0) # updates the values of the keys to 0
    d4 = {}.fromkeys(l,[])
    print(d2)
    print(d3)
    print(d4)

    del d['a']
    print(d)
    d.clear()
    print(d)

    d5 = {'a':[1,2,3],'b':{4,5,6},'c':"hello world",'e':{'x':7,'y':8,'z':9}}
    print(d5['a'][1]) # number 2
    print(4 in d5['b']) # check if 4 in the dictionary
    print(d5['c'][8]) # letter r
        
main()
    
