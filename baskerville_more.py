
def dice(): # prints 2 random numbers, appends to a list
    import random
    l = []
    a = random.randint(1, 6)
    l.append(a)
    b = random.randint(1, 6)
    l.append(b)
    return l

def derivative(l): # from c*x^n to c*n*x^(n - 1)
    l1 = []
    for i in range(1, len(l)):
        c = l[i]
        n = i
        d = c*n
        l1.append(d)
    return l1

def integral(l, a, b):

    A = 0
    B = 0
    for e in range(len(l)):
        c = l[e]
        n = e
        B += c/(n+1)*b**(n+1)
        A += c/(n+1)*a**(n+1)
    return B - A

def avelength(s):
    x = 0
    with open(s, 'r', errors = 'ignore') as f:
        text = f.read()
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace(".", "")
        text = text.replace("\n", "")
        words = text.split(" ") # list
        for word in words:
            x += len(word)
        print(x/len(words))

def longest(s):
    longestword = ""
    longestlength = 0
    with open(s, 'r', errors = 'ignore') as f:
        text = f.read()
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace(".", "")
        words = text.split(" ")
        for word in words:
            if '/n' not in word and " " not in word and "-" not in word:
                longestlength = len(longestword)
                if len(word) > longestlength:
                    longestword = word
                    longestlength = len(longestword)
                
        return longestword, longestlength
            
def main():

    #print(dice())
    l = [1, 2, 3, 4, 5] # 1x^0 + 2x + 3x^2 + 4x^3 + 5x^4
    #print(derivative(l))
    a = 0
    b = 5
    #print(integral(l, a, b))
    s = "thehoundofthebaskervilles.txt"
    #avelength(s)
    print(longest(s))

main()
