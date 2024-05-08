# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:06:38 2012

@author: Radek
"""
from tkinter import * 


# hlavni = Tk()
# v = IntVar() #BooleanVar()
# v.set(1)

# c = Checkbutton(hlavni, text="Přepínač", variable=v) 
# c.grid(row=0,column=1) 

# def tisk():
#     print (v.get())    
    
# tlacitko=Button(hlavni,text="Kontrola",command=tisk)
# tlacitko.grid(row=0,column=0)
 
# mainloop() 
"""
Úkol:
1) Vložte do okna 2 zaškrtávací políčka a tlačítko
   "Inverze", které invertuje u obou políček jejich
   nastavení.
   Nápověda: Využijeme operaci v.set()
"""   
import tkinter as tk

def invert_checkbox_state():
    checkbox1_var.set(not checkbox1_var.get())
    checkbox2_var.set(not checkbox2_var.get())


root = tk.Tk()
root.title("Inverze zaškrtávacích políček")


checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()

checkbox1 = tk.Checkbutton(root, text="Zaškrtávací pole 1", variable=checkbox1_var)
checkbox2 = tk.Checkbutton(root, text="Zaškrtávací pole 2", variable=checkbox2_var)

invert_button = tk.Button(root, text="Inverze", command=invert_checkbox_state)

# Rozmístění prvků v okně
checkbox1.pack()
checkbox2.pack()
invert_button.pack()

root.mainloop()
