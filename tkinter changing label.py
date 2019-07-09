from tkinter import *

def changingwindows():
    UsersName=Name.get()
    Heading.set('HI  '+ UsersName)


#Set up the Tkinter windows
MyWindow = Tk()

MyWindow.geometry('640x480')#sets the size of the window

MyWindow.title('HELLO WORLD')#titles the window

MyWindow.configure(bg='blue')#colors background blue

#creates a variable called Heading to hold the heading text
Heading = StringVar()
Heading.set('please enter your name below')
TitleText = Label (MyWindow,textvariable = Heading,bg='blue',fg='white', font=("Arial", 14)).place(x=200,y=100) #creates text at the top of the window
#ClickImage = PhotoImage(file=
HelloButton = Button (MyWindow,text = 'Click Me',command = changingwindows).place(x=300,y=300) #creates a button
Name=StringVar()
Inputbox=Entry(MyWindow,textvariable=Name,width='25',font=("Arial", 14)).place(x=250,y=200)#this defines the place in the window

MyWindow.mainloop() #Creates the final product


