from tkinter import *
hangman = Tk()
hangman.geometry('885x700')
hangman.title('HANGMAN')
import random
easy = ['active','apple','angry','phone','salt','toilet','math','cake','future','goat','butter','wierd']
medium = ['goodbye','butterfly','english','wizard','doctor','reading','avatar','pokemon','hamster','rocket','online','python','controller']
hard = ['welcome','goodnight','science','download','academy','password','clickbait','defualt','upgrade','describe']
correct = []
incorrect = []
Heading = StringVar()
title = StringVar()
lettersE = StringVar()
dashes = StringVar ()
def board_displaying():
    for i in word:
        if i in correct:
            dashes.set(i, end = ' ')
            TitleText = label(hangman,textvariable = dashes).pack
        else:
            dashes.set('_', end=' ')
            TitleText = label(hangman,textvariable = dashes).place(x=0,y=0)
def player1():
    title.set('please enter a letter')
    def picked_easy():
        word = (random.choice(easy))
        Heading.set(word)
        TitleText = Label (hangman,textvariable = Heading).place(x=200,y=100)
        easy1 = Button (hangman,text = 'EASY',).place(x=1000,y=1000)
        print(word)
    def picked_medium():
        word = (random.choice(medium))
        Heading.set(word)
        TitleText = Label (hangman,textvariable = Heading).place(x=200,y=100)
        print(word)
    def picked_hard():
        word = (random.choice(hard))
        Heading.set(word)
        TitleText = Label (hangman,textvariable = Heading).place(x=200,y=100)
        print(word)
    easy1 = Button (hangman,text = 'EASY',command = picked_easy).place(x=200,y=550)
    medium1 = Button (hangman,text = 'MEDIUM',command = picked_medium).place(x=400,y=550)
    hard1 = Button (hangman,text = 'HARD',command = picked_hard).place(x=600,y=550)
    def board_displaying():
        for i in word:
            if i in correct:
                print(i, end= ' ')
            else:
                print('_', end=' ')
def players2():
    title.set('please enter a word for your oponent to guess')
    TitleText = Label (hangman,textvariable = title).place(x=400,y=100)
def users_word():
    word = own_word.get()
    lettersE.set(word)
    TitleText = Label (hangman,textvariable = lettersE).place(x=600,y=100)
    print(word)
#welcome_to_hangman = PhotoImage(file ="welcome hangmAN.gif")
#x = Label (image = welcome_to_hangman)
#x.grid(row = 0, column = 0)
TitleText = Label (hangman,textvariable = title).place(x=400,y=100)
player1 = Button (hangman,text = '1player',command = player1).place(x=290,y=450)
player2 = Button (hangman,text = '2players',command = players2).place(x=500,y=450)
entering_word = Button (hangman, text = 'ENTER',command = users_word).place(x=800,y=447)
own_word = StringVar()
words = Entry (hangman,textvariable=own_word).place(x=675,y=450)
hangman.mainloop()

hangman_board = ['''
/--------\\
         |
         |
         |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
         |
         |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
         |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
   |     |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|     |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|\    |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|\    |
         |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|\    |
   |     |
         |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|\    |
   |     |
  /      |
         |
_________|___''','''
/--------\\
   |     |
   o     |
  /|\    |
   |     |
  / \    |
         |
_________|___''']
correct = []
incorrect = []
def board ():
    print(hangman_board[len(incorrect)])
    for i in word:
        if i in correct:
            print(i, end= ' ')
        else:
            print('_', end=' ')
    print('\n\n')
    print('*****missed letters*****')
    for i in incorrect:
        print(i, end=' ')
    print('\n************************')

def user_guess ():
    while True:
        guess = input('guess a letter\n')
        if guess in correct or guess in incorrect:
            print ('you already guessed that letter')
        elif len(guess) > 1:
            print ('please enter only one letter at a time')
        elif guess.isnumeric():
            print('please enter only letters')
        elif len(guess) == 0:
            print('please enter a letter')
        else:
            break
    if guess in word:
        correct.append(guess)
    else:
        incorrect.append(guess)

def winning_and_losing():
    if len(incorrect) > 8:
        return'game over'
    for i in word:
        if i not in correct:
            return'not a win'
    return'win'

two_player = input('do you want to play with 2 players:(y/n) ')
if two_player == 'y':
    users_word = input('what word do you want TO PUT IN: (ONLY ONE WORD NO SPACES!!)\n')
    word = users_word
    while True:
        board()
        user_guess()
        win_condition = winning_and_losing()

        if win_condition == 'game over':
            print ('GAME OVER!!!! the word is %s' % word) 
            input('press enter to quit')
            exit()
        elif win_condition == 'win':
            print('YOU WIN!!!!!! the word is %s' % word)
            input('press enter to quit')
            exit()
else:
    print()
    
level = input('pick a level\n ')
if level == 'easy':
    (random.shuffle(easy))
    word = (random.choice(easy))
elif level == 'medium' :
    word = (random.choice(medium))
elif level == 'hard':
    word = (random.choice(hard))
else:
    print ('THAT WAS NOT ONE OF YOUR CHOICES!!')

while True:
    board()
    user_guess()
    win_condition = winning_and_losing()

    if win_condition == 'game over':
        print ('GAME OVER!!!! the word is %s' % word) 
        input('press enter to quit')
        break
    elif win_condition == 'win':
        print('YOU WIN!!!!!! the word is %s' % word)
        input('press enter to quit')
        break
        
