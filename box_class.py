
class box(object):

    def __init__(self, width, length, height):
        self.w = width
        self.l = length
        self.h = height

    def __str__(self):
        return "Box[%f, %f, %f]" % (self.w, self.l, self.h)

    def volume(self):
        return self.w*self.l*self.h

    def surface_area(self):
        return 1.0*(2*(self.w*self.l) + 2*(self.w*self.h) + 2*(self.l*self.h))

    def greater_volume(self, other):
        v1 = self.volume()
        v2 = other.volume()
        if v1 > v2:
            return self
        elif v1 < v2:
            return other
        else:
            return "Same volume"

    def double_box(self):
        return box(2*self.w, 2*self.l, 2*self.h)

    def shift(self, other):
         return box(self.w + other.w, self.l + other.l, self.h + other.h)

    def rescale(self, c):
        return box(self.w/c, self.l/c, self.h/c)


class article(object):

    def __init__(self, text):
        self.text = text
        
    def __str__(self):
        return self.text

    def all_words(self):
        words = self.text.replace(".", "").split(" ")
        return words

    def longest_word(self):
        lw = ""
        L = self.all_words()
        for word in L:
            if len(word) > len(lw):
                lw = word
        return lw

    def most_frequent_character(self):
        d = {}
        for c in self.text:
            if c not in d:
                d[c] = 0
            else:
                d[c] += 1
        E = sorted(d.items(), key = lambda x: x[1], reverse = True)
        return E[0]
                
    def combine(self, other):
        return article(self.text + " " + other.text)

def main():
    box1 = box(1, 4, 5)
    box2 = box(2, 7, 9)
    #print(box1)
    #print(box1.volume())
    #print(box1.surface_area())
    #print(box1.greater_volume(box2))
    #print(box1.double_box())
    #print(box1.shift(box2))
    #print(box1.rescale(10))
    text1 = "Today is Tuesday. What a great day for a day in November."
    text2 = "Two weeks to go!"
    T = article(text1)
    T2 = article(text2)
    #print(T)
    #print(T.all_words())
    #print(T.longest_word())
    #print(T.most_frequent_character())
    #print(T.combine(T2))

main()
