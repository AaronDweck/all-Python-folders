
attempts = 0
password = 'possible'
guess = ''

while attempts <4 and guess != password:
    guess = input("take a guess: ")
    if guess != password:
        print("access denied")
    else:
        print("access granted")

    attempts = attempts + 1

print("thank you for using the program !")

