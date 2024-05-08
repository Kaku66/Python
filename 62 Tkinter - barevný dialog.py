# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:35:00 2013

@author: Radek
"""
# from tkinter import colorchooser
# from tkinter import *


# hlavni=Tk()

# barva=colorchooser.askcolor(title="Barva")
# print (barva)
# #print (barva[0])
# #print (barva[1])
# hlavni["bg"]=barva[1]


# mainloop()

"""
Úkol:
1) Do aplikace vložte tlačítko pro výběr barvy.
   Výběr barvy proveďte pomocí barevného dialogu.
   Vybranou barvu nastavte na pozadí tlačítka.
"""   

from tkinter import colorchooser
from tkinter import *

hlavni = Tk()


def vyber_barvu():
   
    barva = colorchooser.askcolor(title="Vyberte barvu")
    tlacitko["bg"] = barva[1]
    tlacitko.config(bg=barva)
tlacitko = Button(hlavni, text="Vybrat Barvu", command=vyber_barvu)
tlacitko.pack(pady=20)
hlavni.mainloop()


