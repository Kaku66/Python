# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 10:00:12 2013

@author: Radek
"""

# from tkinter import *

# hlavni = Tk()

# def LevyKlik(udalost):
#     print ("Klikl jsi na frame na pozici:", udalost.x, udalost.y)

# def Najeti(udalost):
#     print ("Najel jsi na frame")
# #    print udalost

# def Klavesa(udalost):
#     print ("Stiskl jsi ", udalost.char)
# #    print (udalost)

# def Pohyb(udalost):
#     print (udalost.x, udalost.y)

# def F1(udalost):
#     print ("Stiskl jsi F1")
    
# vstup = Entry(hlavni)
# vstup.bind("<Key>", Klavesa)
# vstup.bind("<F1>",F1)
# vstup.pack()
  
# ramec = Frame(hlavni, width=100, height=100,bg="red")
# ramec.bind("<Button-1>", LevyKlik)
# ramec.bind("<Enter>", Najeti)
# ramec.bind("<B1-Motion>",Pohyb)
# ramec.pack()

# hlavni.mainloop()

"""
1) Vložte do hl. okna frame, který bude reagovat na
   pravé tlačítko myši a vždy si nastaví náhodnou
   barvu pozadí.
2) Při stisku levého tlačítka se nastaví bílé pozadí.
3) Vytvořte program s jedním tlačítkem, které se po
   najetí myši přesune na náhodné místo v okně.
"""   

#1
# import tkinter as tk
# import random

# hlavni_okno = tk.Tk()
# barevny_seznam = ["red", "green", "blue", "yellow", "orange", "purple"]
# frame = tk.Frame(hlavni_okno, width=200, height=200)
# frame.pack()

# def zmen_barvu_pozadi(event):
#     nahodna_barva = random.choice(barevny_seznam)
#     frame.config(bg=nahodna_barva)

# frame.bind("<Button-3>", zmen_barvu_pozadi)
# hlavni_okno.mainloop()



#2
# import tkinter as tk
# import random

# hlavni_okno = tk.Tk()
# hlavni_okno.title("Okno s náhodnou barvou pozadí")

# seznam_barev = ["red", "green", "blue", "yellow", "purple", "orange"]

# def zmen_pozadi_prave(event):
#     nahodna_barva = random.choice(seznam_barev)
#     frame.config(bg=nahodna_barva)

# def zmen_pozadi_leve(event):
#     frame.config(bg="white")

# frame = tk.Frame(hlavni_okno, width=200, height=200)
# frame.pack(padx=20, pady=20)

# frame.bind("<Button-3>", zmen_pozadi_prave)
# frame.bind("<Button-1>", zmen_pozadi_leve)

# hlavni_okno.mainloop()

#3
import tkinter as tk
import random

hlavni_okno = tk.Tk()
hlavni_okno.title("Přesunutí Tlačítka")

tlacitko = tk.Button(hlavni_okno, text="Tlačítko")

def presun_tlacitko_na_nahodne_misto(event):
    nove_x = random.randint(0, hlavni_okno.winfo_width() - tlacitko.winfo_width())
    nove_y = random.randint(0, hlavni_okno.winfo_height() - tlacitko.winfo_height())
    
    tlacitko.place(x=nove_x, y=nove_y)

tlacitko.bind("<Enter>", presun_tlacitko_na_nahodne_misto)
tlacitko.pack()

hlavni_okno.mainloop()








