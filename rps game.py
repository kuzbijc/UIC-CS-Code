import random

def main():

    """
    RULES
    
    paper beats rock
    rock beats scissors
    scissors beats paper
    """

    human = 0
    computer = 0

    print("RPS GAME")
    print("")

    while human < 3 and computer < 3: # while this is true, the game will loop
        a = input("Weapon of choice ((r)ock, (p)aper, (s)cissors): ")
        if a not in ['r', 'p', 's']:
            print("Not an option, try again!")
            break
        b = random.choice(['r', 'p', 's'])
        print("Human chose %s" % (a))
        print("Computer chose %s" % (b))

        if a != b: # the actual game
            if a == 'r':
                if b == 'p':
                    computer += 1
                else:
                    human += 1
            elif a == 'p':
                if b == 'r':
                    human += 1
                else:
                    computer += 1
            else:
                if b == 'r':
                    computer += 1
                else:
                    human += 1
                    
        print("human: %i" % (human))
        print("computer: %i" % (computer))

    if human > computer:
        print("")
        print("gettir dooooone!")
    else:
        print("")
        print("You just got shmashed!")   
        
main()
