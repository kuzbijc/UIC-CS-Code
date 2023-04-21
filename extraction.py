def opening_files(s, p, n):
    pcnt = 0
    ncnt = 0
    neucnt = 0
    with open(s, 'r', errors = 'ignore') as f:
        text = f.read()
        text = text.lower()
        text = text.replace("!", ".")
        text = text.replace("?", ".")
        text = text.replace(";", "")
        text = text.replace("-", " ")
        text = text.replace(",", "")
        text = text.replace("\n", " ")
        text = text.split(".")
    with open(p, 'r') as g:
        pos = g.read()
        pos = pos.replace("\n", " ")
        pos = pos.split(" ")   
    with open(n, 'r') as h:
        neg = h.read() # string
        neg = neg.replace("\n", " ")
        neg = neg.split(" ")
    for sentences in text:
        words = sentences.split(" ")
        intersection_p = set(words).intersection(set(pos))
        intersection_n = set(words).intersection(set(neg))
        if intersection_p > intersection_n:
            pcnt += 1
        elif intersection_p < intersection_n:
            ncnt += 1
        else:
            neucnt += 1
    print("Positive count: %i" % pcnt)
    print("Negative count: %i" % ncnt)
    print("Neutral count : %i" % neucnt)
            
def main():
    s = "thehoundofthebaskervilles.txt"
    p = "positivesentimentwords.txt"
    n = "negativesentimentwords.txt"
    opening_files(s, p, n)

main()
