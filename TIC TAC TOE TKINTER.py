from tkinter import *
#format of the page
TIC_TAC_TOE = Tk()

TIC_TAC_TOE.geometry('450x436')
# proceder for the button
global A
def x_o_placing(player):
    if player == 'X':
        print('hi')
    else:
        A.place(x=1000,y=1000)



TIC_TAC_TOE.title('TIC TAC TOE')
#code for buttons
A = Button(TIC_TAC_TOE,bg = 'grey' , command = x_o_placing('fvf') )
A.config(height = 9 ,width = 20)
A.place(x = 0,y = 0)

B = Button(bg = 'grey')
B.config(height = '9' ,width = '20')
B.place(x = 150,y = 0)

C = Button(bg = 'grey')
C.config(height = 9 ,width = 20)
C.place(x = 300,y = 0)

D = Button(bg = 'grey')
D.config(height = 9 ,width = 20)
D.place(x = 0,y = 145)


E = Button(bg = 'grey')
E.config(height = 9 ,width = 20)
E.place(x = 150,y = 145)

F = Button( bg = 'grey')
F.config(height = 9 ,width = 20)
F.place(x = 300,y = 145)

G = Button(bg = 'grey')
G.config(height = 9 ,width = 20)
G.place(x = 0,y = 290)

H = Button(bg = 'grey')
H.config(height = 9 ,width = 20)
H.place(x = 150,y = 290)

I = Button(bg = 'grey')
I.config(height = 9 ,width = 20)
I.place(x = 300,y = 290)

TIC_TAC_TOE.mainloop()
