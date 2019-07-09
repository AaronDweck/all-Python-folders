from __future__ import division
from random import randint
from os import system
from time import sleep

playing = True
num = randint(1, 100)
guesses = 0


def playagain():
    answer = input("do you want to play again [y/n]? ")
    if (answer .strip() == "y"):
        newgame()
        return True
    elif (answer .strip() == "n"):
        print("thank you for playing") 
        return False
    else:
        return playagain()
    
def newgame ():
    global num
    num = randint(1, 100)
    global guesses
    guesses = 0
    
print ("welcome to my number guessing game!! ")
while(playing):
    print ("please guess a number between 1 and 100")
    guess = int(input("what is your guess"))
    if (guess > 100 or guess < 1):
        invalid = True
        while(invalid):
            print("INVALID NUMBER GUESSED! PLEASE GUESS A VALID NUMBER!")
            guess = int(input("what is your guess"))
            if (100 >= guess >= 1):
                invalid = False
    if (guess == num):

        print("yay you have guessed my number!!") 
        playing = playagain()
    elif  (guess > num):
        print ("your guess was too high try again")
    else:
        print("your guess was too low try again")
