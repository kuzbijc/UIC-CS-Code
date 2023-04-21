
def get_text(s):
    with open(s, 'r',errors = "ignore") as f:
        text = f.read()
    return text

class article(object):

    def __init__(self,text,source):
        self.text = text
        self.source = source

    def __str__(self):
        return "%s\nSource: %s" % (self.text,self.source)

    def num_words(self):
        words =  self.text.split(" ")
        return len(words)

    def num_sentence(self):
        sentences = self.text.split(".")
        return len(sentences)

    def common_word(self):
        words = self.text.split(" ")
        d = {}
        for e in words:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
            a = sorted(d.items(), key = lambda e:e[1], reverse = True)
            most_common = a[0]
        return most_common

    def letter_freq(self):
        d2 = {}
        for letters in self.text.lower():
            if letters not in d2:
                d2[letters] = 1
            else:
                d2[letters] += 1
            letter_freq = sorted(d2.items(), key = lambda e:e[1], reverse = True)
        return letter_freq

    def longer(self,other):
        cwords = self.num_words()
        iwords = other.num_words()
        fwc = self.text.split()[0]
        fwi = other.text.split()[0]
        if cwords > iwords:
            return fwc
        elif cwords < iwords:
            return fwi
        else:
            return "Same length"
        
def main():
    textc = get_text("chicago.txt")
    texti = get_text("illinois.txt")
    a = article(textc,"Wikipedia")
    b = article(texti,"Wikipedia")
    print("Number of words:")
    print(a.num_words())
    print("Number of sentences:")
    print(a.num_sentence())
    print("Most common word:")
    print(a.common_word())
    print("Letter frequency:")
    print(a.letter_freq())
    print("Longer text:")
    print(a.longer(b))
main()
