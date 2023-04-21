
def read_text(s):
    with open(s, 'r', errors = "ignore") as f:
        text = f.read()
    return text

class Text(object):
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return "%s" % self.text

    def num_char(self):
        return len(self.text)

    def num_words(self):
        return len(self.text.split(" "))

    def num_sentences(self):
        return len(self.text.split("."))

    def avg_word_length(self):
        l = []
        words = self.text.split(" ")
        for word in words:
            l.append(len(word))
        return sum(l)/len(l)

class Book(Text): # inheriting a class
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text
        Text.__init__(self,text) # can use methods from other class

class Article(Text): #inheriting a class
    def __init__(self, title, source, date, text):
        self.title = title
        self.source = source
        self.date = date
        self.text = text
        Text.__init__(self,text) # can use methods from other class
        
def main():
    c = "chicago-wikipedia-article.txt"
    h = "thehoundofthebaskervilles.txt"

    a = read_text(c)
    b = read_text(h)
    x = Text(a)
    #print(x)
    #print(x.num_char())
    #print(x.num_words())
    #print(x.num_sentences())
    #print(x.avg_word_length())

    y = Book("The hound of the Baskervilles","Arthur Conan Doyle",b)
    #print(y.num_words())

    z = Article("chicago","wikipedia","on-going",a)
    print(z.num_words())
    
main()
