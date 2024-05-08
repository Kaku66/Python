# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 09:54:43 2013

@author: Radek
"""
"""
Funkce after
- jedná se o časové zpoždění v milisekundách
- je to funkce hlavního okna, volá se tedy hl.after(...)
- po jeho uplynutí času se buď nestane nic (např. hl.after(1000))
- nebo se spustí požadovaná funkce (např. hl.after(1000,funkce))
"""

# from tkinter import messagebox
# from tkinter import *
# import random

# hlavni=Tk()
# hlavni.geometry("250x100")

# def Okno():
#     messagebox.showinfo("Hlášení","Proběhne prodleva 5000 ms") 
#     hlavni.after(3000)
#     hlavni.after(2000)
#     messagebox.showinfo("Hlášení","Proběl časový interval 5000 ms") 

# tlacitko=Button(hlavni,text="Test čekání programu",command=Okno)
# tlacitko.pack()


# def Funkce1():
#     print("Proběhla Funkce1")

# def Funkce2():
#     print("Proběhla Funkce2")

# def TestCasovace():
#     hlavni.after(4000,Funkce1)
#     hlavni.after(3500,Funkce2)

# tlacitko = Button(hlavni, text="Test souběžného spuštění", command=TestCasovace)
# tlacitko.place(relx=0.5, rely=0.5, anchor=CENTER)


# def ZmenBarvu():
#     hexaznaky = "0123456789ABCDEF"
#     barva = "#"
#     for i in range(6):
#         barva += random.choice(hexaznaky)
#     hlavni["bg"] = barva
    
#     hlavni.after(1000, ZmenBarvu)

# ZmenBarvu()
# mainloop()

"""
Úkol:
1) Každou sekundu změňte barevné pozadí hlavního okna.
2) Naprogramujte nastavitelný timer (odpočet), použijte 
   Spinbox. Stačí jeden Spinbox obsahující sekundy.
   Při stisku tlačítka Start se časovač spustí a 
   nepotřebné komponenty se nastaví na "disabled".
   Po uplynutí času se komponenty nastaví opět na 
   "normal".
"""


#1
from tkinter import messagebox
from tkinter import *
import random

hlavni = Tk()
hlavni.geometry("250x100")

# Přidáme globální proměnnou pro ukládání aktuální barvy pozadí
aktualni_barva = "white"

def Okno():
    messagebox.showinfo("Hlášení", "Proběhne prodleva 5000 ms") 
    hlavni.after(3000)
    hlavni.after(2000)
    messagebox.showinfo("Hlášení", "Proběl časový interval 5000 ms") 

tlacitko = Button(hlavni, text="Test čekání programu", command=Okno)
tlacitko.pack()

def Funkce1():
    print("Proběhla Funkce1")

def Funkce2():
    print("Proběhla Funkce2")

def TestCasovace():
    hlavni.after(4000, Funkce1)
    hlavni.after(3500, Funkce2)

tlacitko = Button(hlavni, text="Test souběžného spuštění", command=TestCasovace)
tlacitko.place(relx=0.5, rely=0.5, anchor=CENTER)

def ZmenBarvu():
    global aktualni_barva
    nova_barva = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Náhodná barva v hex formátu
    hlavni.configure(bg=nova_barva)
    aktualni_barva = nova_barva
    hlavni.after(1000, ZmenBarvu)

ZmenBarvu()

mainloop()


#2
# from tkinter import messagebox
# from tkinter import *
# import time

# hlavni = Tk()
# hlavni.geometry("250x100")
# hlavni.title("Nastavitelný timer")

# def uplynul_cas():
#     messagebox.showinfo("Hlášení", "Čas vypršel!")
#     spinbox.config(state=NORMAL)
#     start_tlacitko.config(state=NORMAL)

# def spustit_timer():
#     cas = int(spinbox.get())
#     spinbox.config(state=DISABLED)
#     start_tlacitko.config(state=DISABLED)
#     hlavni.after(cas * 1000, uplynul_cas)

# label = Label(hlavni, text="Vyberte čas v sekundách:")
# label.pack()

# spinbox = Spinbox(hlavni, from_=1, to=300)
# spinbox.pack()

# start_tlacitko = Button(hlavni, text="Start", command=spustit_timer)
# start_tlacitko.pack()

# hlavni.mainloop()







