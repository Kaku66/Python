# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:37:21 2012

@author: Radek
"""
"""
Metoda place
Umožňuje umístění komponenty na konkrétní souřadnice:
a) Absolutní - v pixelech, počítá se z levého horního rohu
   place(x= , y= )
b) Relativní - v desetinných číslech, nejmenší hodnota je 0 a
               největší je 1
   place(relx= , rely= )

Můžeme přidat i parametr anchor, což je kotevní bod komponety.
Jsou tyto: "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
Možno použít i jako N, NE, E, ... (bez uvozovek)

POZOR! V jednom okně nelze kombinovat více zobrazovacích metod!
"""

# from tkinter import *

# hlavni = Tk()

# napis=Label(hlavni,text="Toto je text na abs. souřadnicích")
# napis.place(x=50, y=50, anchor="nw")

# napis2=Label(hlavni,text="Toto je text na relativních. souřadnicích")
# napis2.place(relx=0.5, rely=0.5, anchor="center")

# def Zmena():
#     tlacitko.place(x=200,y=200,width=150,height=80)

# tlacitko=Button(hlavni,text="Konec",command=Zmena)
# tlacitko.place(x=50,y=100,width=100,height=40)
   
# hlavni.mainloop()
"""
Úkol:
1) Stanovte si velikost okna.
   Umístěte do okna tři tlačítka "Konec" na náhodné 
   souřadnice tak, aby nepřekračovalo hranice okna.
   Přidejte tlačítko "Rozmístit" do levého horního rohu.
   Po jeho stisknutí se všem třem tlačítkům nastaví
   nové náhodné souřadnice.
"""   




#1
import tkinter as tk
import random

def rozmistit_tlacitka():
    for tlacitko in tlacitka_list:
        nove_x = random.randint(0, 350)  
        nove_y = random.randint(0, 250)  
        tlacitko.place(x=nove_x, y=nove_y)

okno = tk.Tk()
okno.title("Okno s tlacitky")
okno.geometry("400x300")

tlacitko_konec1 = tk.Button(okno, text="Konec", command=okno.destroy)
tlacitko_konec2 = tk.Button(okno, text="Konec", command=okno.destroy)
tlacitko_konec3 = tk.Button(okno, text="Konec", command=okno.destroy)

tlacitko_rozmistit = tk.Button(okno, text="Rozmístit", command=rozmistit_tlacitka)
tlacitko_rozmistit.place(x=10, y=10)

tlacitka_list = [tlacitko_konec1, tlacitko_konec2, tlacitko_konec3]
for tlacitko in tlacitka_list:
    tlacitko.place(x=random.randint(0, 350),
                   y=random.randint(0, 250))

okno.mainloop()















































# from tkinter import *
# import random as r
# hlavni=Tk() 
# hlavni.minsize(400,400)

# tlacitko1=Button(hlavni,text="Konec",command=hlavni.destroy)
# tlacitko2=Button(hlavni,text="Konec",command=hlavni.destroy)
# tlacitko3=Button(hlavni,text="Konec",command=hlavni.destroy)

# def Rozmistit():
#     tlacitko1.place(x=r.randint(0, 350), y=r.randint(0, 350))
#     tlacitko2.place(x=r.randint(0, 350), y=r.randint(0, 350))
#     tlacitko3.place(x=r.randint(0, 350), y=r.randint(0, 350))

# Rozmistit()

# tlacitko4=Button(hlavni,text="Zamíchej tlačítka",command=Rozmistit)
# tlacitko4.place(x=0, y=0)


# hlavni.mainloop()





