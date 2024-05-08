# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:26:22 2013

@author: Radek
"""
# def Fce():
#     print("Výpis z funkce")

# print(Fce())   


# from tkinter import *
# from tkinter import messagebox

# hl_okno=Tk()          # toto vytvoří hlavní okno

# sez=[]

# def ObsluhaTlacitka(x):
#     messagebox.showinfo("Obsluha","Klikl jsi na tlačítko "+str(x))

# for i in range(20):
#     txt=StringVar()
#     txt.set("Tlačítko "+str(i))
#     b=Button(hl_okno,textvariable=txt,command=lambda x=i:ObsluhaTlacitka(x))
#     sez.append(b)
#     b.pack(fill=BOTH,expand=True)   

# sez[13]["state"]=DISABLED

# for y in range(4): 
#     for x in range(4): 
#         e=Entry(hl_okno)
#         e.grid(row=y, column=x)

# hl_okno.mainloop()


"""
Úkol:
0) Vykreslete tabulku 4x4 z komponent Entry.
1) Pomocí obdobného mechanismu vykreslete tabulku
   o 5-ti sloupcích a 10-ti řádcích složenou z komponent
   Entry + zmenšete šířku. Použijte rozmístění Grid.
2) Vložte do každého políčka jeho souřadnice.
3) Obarvěte políčka v každém řádku náhodnou barvou.
"""    

#0
# import tkinter as tk

# def vytvor_tabulku():
#     root = tk.Tk()
#     root.title("Tabulka 4x4")

#     for i in range(4):
#         for j in range(4):
#             entry = tk.Entry(root, width=10)
#             entry.grid(row=i, column=j, pady=5)

#     root.mainloop()

# vytvor_tabulku()


#1
import tkinter as tk

def vytvor_tabulku():
    root = tk.Tk()
    root.title("Tabulka 5x10")

    for i in range(10):
        for j in range(5):
            entry = tk.Entry(root, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)

    root.mainloop()

vytvor_tabulku()


#2
# import tkinter as tk

# def vytvor_tabulku():
#     root = tk.Tk()
#     root.title("Tabulka 5x10")

#     for i in range(10):
#         for j in range(5):
#             entry_text = f"{i},{j}"
#             entry = tk.Entry(root, width=5)
#             entry.insert(tk.END, entry_text)
#             entry.grid(row=i, column=j, padx=5, pady=5)

#     root.mainloop()

# vytvor_tabulku()



#3
import tkinter as tk
import random

def generuj_nahodnou_barvu():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def vytvor_tabulku():
    root = tk.Tk()
    root.title("Tabulka 5x10")

    for i in range(10):
        for j in range(5):
            entry_text = f"{i},{j}"
            entry = tk.Entry(root, width=5, justify='center')
            entry.insert(tk.END, entry_text)
            entry.grid(row=i, column=j, pady=5)

            # Generování náhodné barvy
            color = generuj_nahodnou_barvu()
            entry.config(bg=color)

    root.mainloop()

vytvor_tabulku()

