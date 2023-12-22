#Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).

from random import randint

def dicecreation():
    print("\nDice game")
    print("Starts in\n3\n2\n1")
    while True:
        print("\nDice Rolling"," you got", randint(1,6),sep = ',')
        if int(input("\nEnter 1 if you want to exit other wise enter 0\t")):
            print("\nThanks for playing this game")
            break
        
dicecreation()
