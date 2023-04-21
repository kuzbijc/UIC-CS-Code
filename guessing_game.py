
"""
GUESS THE WORD GAME
SELECT WORD FROM FILE
ALL WORDS LOWERCASE
SOME WORDS HYPHENATED
10 TRIES TO GUESS CORRECT WORD
"""
import random


def set():
    words = []
    with open("positivesentimentwords.txt", 'r') as f:
        for line in f:
            w = line.replace("\n", "")
            words.append(w)
    n = random.randint(0, len(words) - 1)
    return words[n]

def play():
    randword = set()
    numguess = 10
    guessed = len(randword) * "_"
    lettertried = ""
    print("---------------------")
    print("-GUESS THE WORD GAME-")
    print("It's a(n) %i letter word." % len(randword))
    print("---------------------")
    while numguess > 0:
        print("Number of tries remaining: %i" % numguess )
        print("---------------------")
        print("Letters already tried: ", lettertried)
        print("Current State: ", guessed)
        print("---------------------")
        print("")
        if "_" in guessed:
            letter = input("Choose a letter bro: ")
            lettertried += letter
            if letter in randword:
                for i in range(len(randword)):
                    if letter == randword[i]:
                        temp = list(guessed)
                        temp[i] = letter
                        guessed = "".join(temp)
                        print(guessed)
            else:
                numguess -= 1
        else:
            break
    if numguess == 0:
        print("You lose!")
        print("The word was: %s" % randword)
    else:
        print("You won!")
        
                              
def main():

    randword = set()
    play()


main()
