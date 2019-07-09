from random import *
from time import *
import sys
a='a'
b='b'
c='c'
d='d'
e='e'
f='f'
g='g'
h='h'
i='i'

x_o = ' '

letters = ['a','b','c','d','e','f','g','h','i']

turns = True

def game_board():
    print(a,'|',b,'|',c)
    print('---------')
    print(d,'|',e,'|',f)
    print('---------')
    print(g,'|',h,'|',i)
    print()

def moving(x_o):
    turns = True
    x_turn = input ('where do you want to move? ')
    if x_turn == 'a':
        global a
        if a == 'X' or a == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            a = x_o
    elif x_turn == 'b':
        global b
        if b == 'X' or b== 'O':
            print('you cant go there')
            moving(x_o)
        else:
            b = x_o
    elif x_turn == 'c':
        global c
        if c == 'X' or c == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            c = x_o
    elif x_turn == 'd':
        global d
        if d == 'X' or d == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            d = x_o
    elif x_turn == 'e':
        global e
        if e == 'X' or e == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            e = x_o
    elif x_turn == 'f':
        global f
        if f == 'X' or f == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            f = x_o
    elif x_turn == 'g':
        global g
        if g == 'X' or g == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            g = x_o
    elif x_turn == 'h':
        global h
        if h == 'X' or h == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            h = x_o
    elif x_turn == 'i':
        global i
        if i == 'X' or i == 'O':
            print('you cant go there')
            moving(x_o)
        else:
            i = x_o
    else:
        print ('that is not a choice')
        moving(x_o)

def comp_moving():
    turns = True
    o_turn = choice(letters)
    if o_turn == 'a':
        global a
        if a == 'X' or a == 'O':
            comp_moving()
        else:
            a = 'O'
    elif o_turn == 'b':
        global b
        if b == 'X' or b == 'O':
            comp_moving()
        else:
            b = 'O'
    elif o_turn == 'c':
        global c
        if c == 'X' or c == 'O':
            comp_moving()
        else:
            c = 'O'
    elif o_turn == 'd':
        global d
        if d == 'X' or d == 'O':
            comp_moving()
        else:
            d = 'O'
    elif o_turn == 'e':
        global e
        if e == 'X' or e == 'O':
            comp_moving()
        else:
            e = 'O'
    elif o_turn == 'f':
        global f
        if f == 'X' or f == 'O':
            comp_moving()
        else:
            f = 'O'
    elif o_turn == 'g':
        global g
        if g == 'X' or g == 'O':
            comp_moving()
        else:
            g = 'O'
    elif o_turn == 'h':
        global h
        if h == 'X' or h == 'O':
            comp_moving()
        else:
            h = 'O'
    elif o_turn == 'i':
        global i
        if i == 'X' or i == 'O':
            comp_moving()
        else:
            i = 'O'
    else:
        print ()
    sleep(2)

def CI():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    if(a=='X' and a==b and c=='c'):
        c = 'O'
    elif(a=='X' and a==c and b=='b'):
        b = 'O'
    elif(b=='X' and b==c and a=='a'):
        a = 'O'
    elif(d=='X' and d==e and f=='f'):
        f = 'O'
    elif(d=='X' and d==f and e=='e'):
        e = 'O'
    elif(e=='X' and e==f and d=='d'):
        d = 'O'
    elif(g=='X' and g==h and i=='i'):
        i = 'O'
    elif(g=='X' and g==i and h=='h'):
        h = 'O'
    elif(h=='X' and h==i and g=='g'):
        g = 'O'
    elif(a=='X' and a==d and g=='g'):
        g = 'O'
    elif(a=='X' and a==g and d=='d'):
        d = 'O'
    elif(d=='X' and d==g and a=='a'):
        a = 'O'
    elif(b=='X' and b==e and h=='h'):
        h = 'O'
    elif(b=='X' and b==h and e=='e'):
        e = 'O'
    elif(e=='X' and e==h and b=='b'):
        b = 'O'
    elif(c=='X' and c==f and i=='i'):
        i = 'O'
    elif(c=='X' and c==i and f=='f'):
        f = 'O'
    elif(f=='X' and f==i and c=='c'):
        c = 'O'
    elif(a=='X' and a==e and i=='i'):
        i = 'O'
    elif(a=='X' and a==i and e=='e'):
        e = 'O'
    elif(e=='X' and e==i and a=='a'):
        a = 'O'
    elif(c=='X' and c==e and g=='g'):
        g = 'O'
    elif(c=='X' and c==g and e=='e'):
        e = 'O'
    elif(e=='X' and e==g and c=='c'):
        c = 'O'
    else:
        comp_moving()
       
        
def computer_winning():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    if(a=='O' and a==b and c=='c'):
        c = 'O'
    elif(a=='O' and a==c and b=='b'):
        b = 'O'
    elif(b=='O' and b==c and a=='a'):
        a = 'O'
    elif(d=='O' and d==e and f=='f'):
        f = 'O'
    elif(d=='O' and d==f and e=='e'):
        e = 'O'
    elif(e=='O' and e==f and d=='d'):
        d = 'O'
    elif(g=='O' and g==h and i=='i'):
        i = 'O'
    elif(g=='O' and g==i and h=='h'):
        h = 'O'
    elif(h=='O' and h==i and g=='g'):
        g = 'O'
    elif(a=='O' and a==d and g=='g'):
        g = 'O'
    elif(a=='O' and a==g and d=='d'):
        d = 'O'
    elif(d=='O' and d==g and a=='a'):
        a = 'O'
    elif(b=='O' and b==e and h=='h'):
        h = 'O'
    elif(b=='O' and b==h and e=='e'):
        e = 'O'
    elif(e=='O' and e==h and b=='b'):
        b = 'O'
    elif(c=='O' and c==f and i=='i'):
        i = 'O'
    elif(c=='O' and c==i and f=='f'):
        f = 'O'
    elif(f=='O' and f==i and c=='c'):
        c = 'O'
    elif(a=='O' and a==e and i=='i'):
        i = 'O'
    elif(a=='O' and a==i and e=='e'):
        e = 'O'
    elif(e=='O' and e==i and a=='a'):
        a = 'O'
    elif(c=='O' and c==e and g=='g'):
        g = 'O'
    elif(c=='O' and c==g and e=='e'):
        e = 'O'
    elif(e=='O' and e==g and c=='c'):
        c = 'O'
    else:
        CI()
def winner(x_o):
    if (a==b and a==c) or (a==d and a==g) or (a==e and a==i) or (b==e and e==h) or (c==f and c==i) or (c==e and c==g) or (g==h and g==i)or (d==e and d==f):
        game_board()
        print (x_o,'wins')
        sleep(1)
        sys.exit()
    elif a == 'a' or b == 'b' or c == 'c' or d == 'd' or e == 'e' or f == 'f' or g == 'g' or h == 'h' or i == 'i':        
        print()
    else:
        print ('its a tie')
        sys.exit()

playing_1_2=input('do you want to play with one player or two player ')

if playing_1_2 == '1':
    while turns == True: 
        game_board()
        moving('X')
        winner('X')
        game_board()
        computer_winning()
        winner('O')
    
    
elif playing_1_2 == '2':
    while turns == True:
        game_board()
        moving('X')
        winner('X')
        game_board()
        moving('O')
        winner('O')
else:
    print()
