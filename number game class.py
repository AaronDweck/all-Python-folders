
import random

print("welcome to guess my number")

print()
the_number = random.randint(1,100)

guess = int(input("take a guess between (1,100): "))

numberofguesses = 1
   
while guess != the_number:
    if guess < the_number:
        print("go higher")
    else:
        print("go lower")


    guess = int(input("take a guess: "))
    numberofguesses = numberofguesses + 1

print()
print("you guessed it! the number was", the_number)
print("and it only took you", numberofguesses, "attemts!\n")

input("\n\npress the enter key to exit.")
