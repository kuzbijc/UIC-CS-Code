
def frequency(s):

        with open(s, 'r', errors = 'ignore') as f:
            text = f.read()
            text = text.replace("\n", " ") # replacing with white space
            text = text.replace(".", " ")
            text = text.replace("?", " ")
            text = text.replace("!", " ")
            text = text.replace("-", " ")
            text = text.replace("{", " ")
            text = text.replace(")", " ")
            text = text.replace(",", " ")
        text = text.lower()
        words = text.split(" ")

        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        e = sorted(d.items(), key = lambda x: x[1]) # list of key, value

        #for i in e:
            #print(i)

def main():

    d ={} # empty dictionary
    d = {"January": 1, "February": 2, "March": 3, "April": 4}  # {key1: value1, key2: value2,...}
    #print(d)
    #print(len(d)) # 2 elements in dictionary

    d["May"] = 5 # "May": 5 added to dictionary
    d.update({"June": 6}) # "June": 6 added to dictionary
    #print(d)
    
    #print(d.keys()) # prints keys in dictionary
    #print(d.values()) # prints values in dictionary

    #for k in d:
        #print(k, d[k]) # prints the key and value

    del d["June"] # deletes the value and key for June
    #print(d)

    #print(d["January"]) # returns the value of January
    
    #print("January" in d) # checks if key is in dictionary

    frequency("thehoundofthebaskervilles.txt")


main()
