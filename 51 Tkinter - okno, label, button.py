# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:18:37 2012

@author: Martin
"""
"""
Vše lze nalézt na:
http://tkinter.programujte.com (pro Python 2)

http://tkinter.py.cz (pro Python 3, musí být http:// !!!)
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-knihovna-tkinter/
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-menu-v-knihovne-tkinter/
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-knihovna-tkinter-3-cast/

fce Tk() - založí hlavní okno programu
fce mainloop() - zobrazí okno a čeká na uživatele
"""

# from tkinter import *

# hl_okno=Tk()          # toto vytvoří hlavní okno


# hl_okno.title("Výuková aplikace")

# hl_okno.minsize(300,200)
# hl_okno.maxsize(400,300)
# #hl_okno.geometry("400x300")

# hl_okno.resizable(False,False)

# data = "123"

# def zmen_napis():
#     global data
#     napis.configure(text="Jiny napis", fg="blue")

# def zmen_napis2():
#     global data
#     print (napis["text"])
#     napis["text"]=napis["text"]+"!"
#     napis["fg"]="black"
#     tlacitko3["command"]=hl_okno.destroy

# napis=Label(hl_okno,text="Popisek v Labelu",fg="red", bg="#00FF00", font=("Arial",25))  # label napis
# napis.pack()    

# tlacitko1=Button(hl_okno, text="Vypnout",command=hl_okno.destroy )
# tlacitko1.pack() 

# tlacitko2=Button(hl_okno, text="Změna nápisu", width=30, height=3,command=zmen_napis)
# tlacitko2.pack() 

# tlacitko3=Button(hl_okno, text="Druhá změna nápisu", width=30, height=3,command=zmen_napis2)
# tlacitko3.pack() 


# hl_okno.mainloop() #nekonečná smyčka, čeká na události od uživatele

"""
Úkol:
1) Naprogramujte počítač kliknutí.
   Bude obsahovat 4 tlačítka a 1 label s číslem:
       - plus
       - minus
       - reset
       - end
   Pozor, budeme-li pracovat s proměnnými, musíme použít global!!!
    
2) Naprogramujte generátor příkladů na násobení.
   Na stisk tlačítka se vygeneruje náhodný příklad a 
   zobrazí se pomocí labelu.
 """

#1
import tkinter as tk

counter_value = 0

def operate(value):
    global counter_value
    counter_value += value
    label.config(text=str(counter_value))

def end_program():
    root.destroy()

root = tk.Tk()
root.title("Počítadlo")

label = tk.Label(root, text=str(counter_value))
label.pack()

buttons = [("Plus", 1), ("Minus", -1), ("Reset", 0), ("End", None)]
for text, value in buttons:
    tk.Button(root, text=text, command=lambda v=value: 
              (operate(v) if v is not None else end_program())).pack(side=tk.LEFT)

root.mainloop()


# #2
# import tkinter as tk
# from random import randint

# root = tk.Tk()
# root.title("Generátor násobení")        

# example_label = tk.Label(root, text="", font=("Helvetica", 16))
# example_label.pack(pady=20)

# generate_button = tk.Button(root, text="Generovat příklad", command=lambda: example_label.config(text=f"{randint(1, 10)} * {randint(1, 10)} = ?"))
# generate_button.pack()

# root.mainloop()