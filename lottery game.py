
import random

"""
LOTTERY GAME
RULES

pick 5: 1 - 70
pick mega 1: 1 - 25
"""

def one():
    g = random.sample(range(1, 71), 5)
    g.sort()
    m = random.randint(1, 25)
    g.append(m)
    return g

def many(n):
    gamecount = 0
    while True:
        g = one()
        print("games played: ", gamecount)
        print(n)
        print(g)
        if n == g:
            print("JACKPOT!")
            break
        print("------------------------")    
        gamecount += 1
    

def main():

    n = [5, 11, 7, 38, 70, 6]
    many(n)
    


main()
