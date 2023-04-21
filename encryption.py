def encryption(s, n):

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s1 = ""
    for c in s:
        if c == ' ':
            s1 += c
        else:
            i = a.index(c)
            s1 += a[(i + n) % 26]
    return s1 + str(n)

def decryption(E):
    s = ""
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d = ""
    for c in E:
        if c in "0123456789":
            s += c
    n = int(s)
    for i in range(len(E)):
        c = E[i]
        if c in a:
            b = a.index(c)
            d += a[(b - n) % 26]
        if c == " ":
            d += " "
    return d

def main():
    E = encryption("hello world", 1)
    print(E)
    D = decryption(E)
    print(D)

main()
