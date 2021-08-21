#Imports 
from tkinter import *
import os
from PIL import ImageTk, Image


#Main Screen
master=Tk()
master.title("Banking management system")

#Functions
def register():

    #Varibles
    temp_Name = StringVar()
    temp_Age = StringVar()
    temp_Gender = StringVar()
    temp_Mobile_no = StringVar()
    temp_Password = StringVar()


    
    #Register screen
    register_screen=Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen,text="Please enter your details below",font=('calibri',12)).grid(row=0,sticky=W,pady=10)
    Label(register_screen,text="Name",font=('calibri',12)).grid(row=1,sticky=W)
    Label(register_screen,text="Age",font=('calibri',12)).grid(row=2,sticky=W)
    Label(register_screen,text="Gender",font=('calibri',12)).grid(row=3,sticky=W)
    Label(register_screen,text="Mobile no ",font=('calibri',12)).grid(row=4,sticky=W)
    Label(register_screen,text="Password",font=('calibri',12)).grid(row=5,sticky=W)


    #Entires
    Entry(register_screen,textvariable=temp_Name).grid(row=1,column=1)
    Entry(register_screen,textvariable=temp_Age).grid(row=2,column=1)
    Entry(register_screen,textvariable=temp_Gender).grid(row=3,column=1)    
    Entry(register_screen,textvariable=temp_Mobile_no).grid(row=4,column=1)
    Entry(register_screen,textvariable=temp_Password).grid(row=5,column=1)   
    
    
def login():
    print("This is a login page")
    


#Import image 

img=Image.open('IMAGE1.png')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

#Labels 

Label(master , text = "Coustom Banking Beta", font=('calibir',14)).grid(row=0,pady=10,sticky = N)
Label(master , text = "Welcome", font=('calibir',12)).grid(row=1,sticky = N)
Label(master , text = "The most secure bank you've probably used", font=('calibir',12)).grid(row=2,sticky = N)
Label(master , image=img, font=('calibir',14)).grid(row=3,pady=15,sticky = N)





#Adding buttons

Button(master , text="Register",font=('calibir',12),width=20,command=register).grid(row=4,pady=10,sticky = N)

Button(master , text="Login",font=('calibir',12),width=20,command=login).grid(row=5,pady=10,sticky = N)

master.mainloop()

