def asuh(): # adding shit to a file without deleting the original shit
    #with open("asuh.txt", 'a')as f:
    #    f.write("not much, you? \n")
    with open("asuh.txt", 'r') as f: # opening file, reading, counting number of words
        text = f.read()
        #text = text.replace("\n, " ")
        L = text.split(" ")
        print(L) 

def main():
    #asuh()
    

main()
