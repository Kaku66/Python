# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 10:47:54 2012

@author: Radek
"""

# from tkinter import *

# hl_okno=Tk()          # toto vytvoří hlavní okno

# jmeno=Label(hl_okno, text="Zadej jméno:")
# jmeno.grid(row=0,sticky=E)         
# prijmeni=Label(hl_okno, text="Zadej příjmení:")
# prijmeni.grid(row=1,sticky=E)  
# vstup1=Entry(hl_okno)
# vstup1.grid(row=0,column=1)         
# vstup2=Entry(hl_okno)
# vstup2.grid(row=1,column=1)         

# kontrola=Label(hl_okno,text="")
# kontrola.grid(row=2,columnspan=2)

# def Zkontroluj():
#     ret1=vstup1.get()
#     ret2=vstup2.get()
#     ret3=ret1+" "+ret2
#     kontrola["text"]=ret3

# tlacitko1=Button(hl_okno,text="Kontrola",command=Zkontroluj)
# tlacitko1.grid(row=3)
# tlacitko2=Button(hl_okno,text="Kontrola",command=Zkontroluj)
# tlacitko2.grid(row=4,sticky=W+E)

# tlacitko3=Button(hl_okno,text="Konec",command=hl_okno.destroy)
# tlacitko3.grid(row=3,column=1,rowspan=2, sticky=W+E+N+S)

# hl_okno.mainloop() 


"""
Úkol:
1) Rozmístěte tlačítka a ostatní komponenty jako na
   kalkulačce pomocí rozmístění GRID 
   (P:\stejskal\Python\Cvičení Tkinter\cv2 - grid.jpg).
"""      

#1
import tkinter as tk

def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def clear():
    entry_var.set("")

# Vytvoření okna
window = tk.Tk()
window.title("Tk - Kalkulačka")

title_label = tk.Label(window, text="Kalkulačka", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=4)

# Vytvoření vstupního pole
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 14), bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=1, column=0, columnspan=4)

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "=",
    "0", ","
]

# Přidání tlačítek pomocí cyklu
row_val = 2
col_val = 0

for button in buttons:
    if button == "0":
        tk.Button(window, text=button, padx=50, pady=20, font=("Arial", 14), command=lambda b=button: on_button_click(b) if b != "=" else calculate()).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 2
    elif button == "=":
        tk.Button(window, text=button, padx=20, pady=63, font=("Arial", 14), command=lambda b=button: on_button_click(b) if b != "=" else calculate()).grid(row=row_val, column=col_val, rowspan=2)
        col_val += 1
    else:
        tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 14), command=lambda b=button: on_button_click(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
        col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()










