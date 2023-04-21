"""
PICKLE
like a database
"serialize" and "de-serialize" data
can restore functions
cannot restore classes
preserves structure of the code
allows you to send code to someone
you pickle it (output only)
they unpickle it (output only)
"""
import pickle

def main():
    A={1,2,3}
    B={4,-7,-5}
    C=A.union(B)

    #serialization: pickle data to file
    with open("output.p",'wb') as f: #wb=write in binary
        pickle.dump([A,B,C],f) #writing data to f

    #deserialization: unpickle from file
    with open("output.p",'rb') as f: #rb=read in binary
        pA,pB,pC=pickle.load(f) #accessing individual elements of the list
        print(pA)
        print(pB)
        print(pC)
        print(type(pC))
        
main()
