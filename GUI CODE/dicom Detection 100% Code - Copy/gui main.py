# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
#from pymsgbox import *


root=tk.Tk()

root.title("Dicom Detection ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"D3NEW4.jpg")
bg.resize((1366,500),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="DICOME DETECTION",width=40,background="#800000",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800000")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login1.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......DICOM IMAGE PROCESSING USING DEEP LEARNING FOR CHEST X-RAYS ......",width=85,height=3,background="#800000",foreground="white",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=685)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="#800000",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1000,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="#800000",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1100,y=18)



root.mainloop()
