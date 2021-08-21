#Imports 
from tkinter import *
import os
from PIL import ImageTk, Image
master=Tk()
master.title("Banking management system")


#Import image 

img=Image.open('IMAGE1.png')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

#Labels 

Label(master , text = "Coustmer Banking System", font=('calibir',14)).grid(row=0,Sticky=N,pady=10)
Label(master , text = "Welcome", font=('calibir',14)).grid(row=1,Sticky=N)
Label(master , image=img, font=('calibir',14)).grid(row=2,Sticky=N,pady=15)



