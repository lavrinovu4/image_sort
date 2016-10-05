#!/usr/bin/python3

import tkinter
from tkinter import messagebox

top = tkinter.Tk()

top.title("Huge test")
top.geometry('{}x{}'.format(1000, 300))

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()

top.mainloop()

