from tkinter import *
import tkinter
#Parent Window Setup
GoodChefWindow = Tk()
GoodChefWindow.title("Welcome To GoodChef")
GoodChefWindow.geometry("600x500")

#Pickup and Delivery buttons
def Delivery_Clicked():
    Delivery=Tk()
    Delivery.title("Delivery Options")
    Delivery.geometry("400x333")
    Remove_Buttons()

def PickUp_Clicked():
    Delivery=Tk()
    Delivery.title("Pick Up Options")
    Delivery.geometry("400x333")
    Remove_Buttons()

def Remove_Buttons():
    MenuButtonsFrame.destroy()

def Buttons():    
    MenuButtonsFrame = LabelFrame(GoodChefWindow, text="Order").pack()
    DeliveryLabelFrame = LabelFrame(MenuButtonsFrame)
    DeliveryLabelFrame.pack(side=RIGHT,expand="yes")
    PickUpLabelFrame = LabelFrame(MenuButtonsFrame)
    PickUpLabelFrame.pack(side=LEFT,expand="yes")
    DeliveryButton = tkinter.Button(DeliveryLabelFrame,bg="red",
                                    fg="yellow",compound="left",
                                    width=120,text="Delivery",
                                    command=Delivery_Clicked())
    PickUpButton = tkinter.Button(PickUpLabelFrame,bg="red",
                                  fg="yellow",compound="left",
                                  width=120,text="Pick Up",
                                  command=PickUp_Clicked())
    DeliveryButton.pack()
    PickUpButton.pack()

Buttons()
