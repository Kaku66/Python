# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:24:22 2012

@author: Radek
"""

# from tkinter import *

# okno = Tk()
# okno.geometry("200x100")
# okno["bg"]="red"

# promenna = StringVar()
# promenna.set("Vyber volbu") # standardní hodnota

# def test(hodnota):
#     print ("hodnota je:", hodnota)
#     # print ("hodnota je:", promenna.get())

# sez=["jedna", "dva", "tři","čtyři"]

# w = OptionMenu(okno, promenna,*sez,command=test)
# w.pack(side="left")

# mainloop()

"""
1) Vytvořte rozbalovací nabídku s třemi barvami a při
   výběru nastavte danou barvu na pozadí okna.

   Zkuste použít slovník:
   barvy={"červená":"#ff0000","bílá":"#ffffff"}
   okno["bg"]=barvy[promenna.get()]
"""   



#1
import tkinter as tk

okno = tk.Tk()
okno.title("Rozbalovací nabídka s barvami")

def zmen_barvu():
    vybrana_barva = promenna.get()
    if vybrana_barva in barvy:
        okno["bg"] = barvy[vybrana_barva]

barvy = {"červená": "#ff0000", "bílá": "#ffffff", "modrá": "#0000ff"}
promenna = tk.StringVar(okno)
promenna.set("Vyberte barvu")

rozbalovaci_nabidka = tk.OptionMenu(okno, promenna, *barvy)
rozbalovaci_nabidka.pack(pady=10)

tlacitko = tk.Button(okno, text="Změnit barvu", command=zmen_barvu)
tlacitko.pack(pady=10)

okno.mainloop()




