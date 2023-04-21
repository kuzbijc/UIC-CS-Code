
def holmes(file1):

    cnt = 0
    with open(file1, 'r', errors = 'ignore') as f:
        text = f.read()
        text= text.replace("?", ".").replace("!", ".")
        sentences = text.split(".") # returns a list of sentences
        #print(len(sentences))
        for sentence in sentences:
            if 'Holmes' and 'Watson' in sentence:
                cnt += 1
        print(cnt)


def palindrome(s): # checks palindrome

    r = ""
    for i in range(1, len(s)+1):
        r += s[-i]
    if s == r:
        print(True)
    else:
        print(False)

def vowelfreq(file1):

    d = {}
    
    with open(file1, 'r', errors = 'ignore') as f:
        text = f.read()
        text = text.lower() # string
    for c in text:
        if c in "aeiou":
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d        
                
        
def cointoss():
    
    import random
    return random.choice(['h', 't'])     


def main():

    file1 = "thehoundofthebaskervilles.txt"
    #holmes(file1)
    s = "kayak"
    #palindrome(s)
    #print(vowelfreq(file1))
    print(cointoss())
    




main()
