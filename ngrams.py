
#Markov model: bigrams/trigrams

def genngram(text, n):
    l = text.split(" ") # l = ["hello", "my", "name", "is", "my", "name", "is"]
    ngram = []
    for i in range(len(l)- (n - 1)):
        s = ""
        for j in range(n):
            s += l[i + j] + " "
        ngram.append(s[: -1])
    return list(set(ngram))

def gettext(s):
    with open(s, 'r', errors = 'ignore') as f:
        text = f.read()
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("\n", " ")
    text = text.lower()
    return text

def gram2dict(text, ngram):
    d = {} # {"the way": 24}
    for e in ngram:
        d[e] = text.count(e)
    return d

def dictsort(d):
    e = sorted(d.items(), key = lambda x: x[1])
    for i in e:
        print(i)

def main():
    s = "thehoundofthebaskervilles.txt"
    text = gettext(s)
    ngram = genngram(text, 3)
    #print(ngram)
    d = gram2dict(text, ngram)
    #print(d)
    dictsort(d)

main()
