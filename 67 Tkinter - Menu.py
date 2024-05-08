# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:21:14 2013

@author: Radek
"""

# from tkinter import *
# from tkinter import messagebox
# hlavni = Tk()
# hlavni.minsize(width=300,height=80)

# HorniMenu=Menu(hlavni)
# MaleMenu=Menu(hlavni)

# def Soubor():
#     messagebox.showinfo("Soubor","Tato část není naprogramována!")
    
# HorniMenu.add_command(label="Soubor",command=Soubor)
# HorniMenu.add_command(label="Nastavení",command=Soubor)
# HorniMenu.add_command(label="Nápověda",command=Soubor)
# HorniMenu.add_command(label="Konec",command=hlavni.destroy)

# MaleMenu.add_command(label="Soubor",command=Soubor)
# MaleMenu.add_command(label="Konec",command=hlavni.destroy)

# hlavni.config(menu=HorniMenu)

# def ZmenMenu():
#     hlavni.config(menu=MaleMenu)  

# b1=Button(hlavni,text="Menu1",command=lambda:(hlavni.config(menu=HorniMenu)))
# b1.pack()
# b2=Button(hlavni,text="Menu2",command=ZmenMenu)
# b2.pack()

# print(b1["command"])
# print(b2["command"])

# mainloop()

"""
Úkol:
1) Vytvořte v aplikaci horní menu s položkami Červená, Zelená a 
   Konec. První dvě položky nastaví barvu na pozadí okna,
   poslední ukončí aplikaci.
"""

#1
import tkinter as tk

okno = tk.Tk()
okno.title("Menu s barvami")
horni_menu = tk.Menu(okno)

def nastav_barvu(barva):
    okno.configure(bg=barva)

def ukoncit_aplikaci():
    okno.destroy()

podmenu_barvy = tk.Menu(horni_menu)
podmenu_barvy.add_command(label="Červená", command=lambda: nastav_barvu("red"))
podmenu_barvy.add_command(label="Zelená", command=lambda: nastav_barvu("green"))

horni_menu.add_cascade(label="Barvy", menu=podmenu_barvy)
horni_menu.add_command(label="Konec", command=ukoncit_aplikaci)

okno.config(menu=horni_menu)
okno.mainloop()

     