print ("welcome to my chat box")

print()
password = 'aarondweck24'
guess = input ('please enter pasword: ')

while guess != password:
    print('access denied')
    guess = input('pleas try again')
print('access granted')

print() 
yourname = input ("so, what is your name? ")
print("welcome ", yourname)

print()
age = int(input("how old are you? "))
if age == 12:
    print("same as me")
else:
    print("sorry you belong in that group")

print()
live = input("where do you live? ")
if live == "london":
    print("thats realy cool")
elif live == "maida vale":
    print("that is nice")
else:
    print("i dont believe you")

print()
school = input("what school do you go to? ")
if school == "hasmonean":
    print("oh wow i feel so bad for you")

elif school == "jfs":
    print("wow realy!")

else:
    print("oh wow that sucks")

print()
color = input("what is your favourite color? ")
if color == "red":
    print("wow thats mine to!")
elif color == "blue":
    print("ok that is cool")
elif color == "green":
    print("that is a cool color")
else:
    print("that is not a color i like")
    
print()
house = input("do you like your house? ")
if house == "yes":
    print(" cooooool")
elif house == "no":
    print ("oh thats sad")
else:
    print ("ok i understand")

print()
my_thoughts="food"

guess = input("can you geuss what i am thinking of? ")

if guess != my_thoughts:
    print("wrong try again. ")
else:
    print("winner!")
