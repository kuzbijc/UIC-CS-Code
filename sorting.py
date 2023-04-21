
def main():
    l = [['a',1],['b',2],['c',0]]
    print(sorted(l, key = lambda x: x[1]))

    a = ['hello','world','how','do','you','like','me','now']
    print([e[0] for e in a]) # first letter of each string

main()
