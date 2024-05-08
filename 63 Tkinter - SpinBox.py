# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 11:49:29 2013

@author: Radek
"""

# from tkinter import *

# hlavni=Tk()
# hlavni.geometry("250x100")
# hodnota=StringVar()
# hodnota.set(0)

# def Nastav():
#     l["text"]=hodnota.get()
    
# w = Spinbox(hlavni, from_=-50, to=1000, increment=2,textvariable=hodnota,command=Nastav)
# w.pack()

# l=Label(text="0",font="Arial 20")
# l.pack()

# hlavni.mainloop()

"""
Úkol:
1) Pomocí Spinboxu zkuste měnit velikost písma u Labelu.
"""    

from tkinter import *

hlavni = Tk()
hlavni.geometry("250x100")
hodnota = StringVar()
hodnota.set(0)

def Nastav():
    velikost_pisma = int(hodnota.get())
    novy_font = f"Arial {velikost_pisma}"
    l.config(font=(novy_font))

w = Spinbox(hlavni, from_=-50, to=1000, increment=2, textvariable=hodnota, command=Nastav)
w.pack()

l = Label(text="0", font="Arial 20")
l.pack()

hlavni.mainloop()


