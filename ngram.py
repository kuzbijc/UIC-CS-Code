
def genngram(s1, n):
    l = s1.split(" ")  # l = ["hello", "my", "name", "is", "my", "name", "is"]
    ngram = []
    for i in range(len(l) - (n - 1)):
        s = ""
        for j in range(n):
            s += l[i + j] + " "
        ngram.append(s[:-1])
    return set(ngram)

def gettext(s):
    cnt = 0
    d = {}
    n = ['!', '?', ","]
    with open(s, 'r', errors='ignore') as f:
        text = f.read()
    text = text.replace(str(n), " ")
    text = text.lower()
    return text

def ngrams_to_dictionary(text,ngrams):
   D={}
   cnt=0
   for e in ngrams:
    D[e]=text.count(e)
   return D

def sort_dictionary(D):
    E=sorted(D.items(),key=lambda x: x[1],reverse=True)
    for e in E:
        print(e)
        
def main():
    s1 = "hello my name is jakub"
    #s = "thehoundofthebaskervilles.txt"
    print(genngram(s1, 2))
    #text = gettext(s)
    #ngram = genngram(text, 2)
    #print(ngram)
    #D=ngrams_to_dictionary(text,ngram)
    #print(D)
    #sort_dictionary(D)

main()
