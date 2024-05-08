# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:35:54 2013

@author: Radek
"""


# from tkinter import *
# from tkinter import messagebox
# hlavni = Tk()

# #vytvoření jednotlivých menu
# HorniMenu=Menu(hlavni)
# MenuSoubor=Menu(HorniMenu,tearoff=0)
# # VnoreneMenu = Menu(MenuSoubor,tearoff=0)

# def Soubor():
#     messagebox.showinfo("Soubor","Tato část není naprogramována!")

# #vytvoření jedné rozbalovací nabídky a připojení do hl. menu 
# MenuSoubor.add_command(label="Otevřít",command=Soubor)
# MenuSoubor.add_command(label="Uložit",command=Soubor)
# # MenuSoubor.add_cascade(label="Další menu", menu = VnoreneMenu)
# MenuSoubor.add_separator()
# MenuSoubor.add_command(label="Konec",command=hlavni.destroy)


# # VnoreneMenu.add_command(label="Položka1",command=Soubor)
# # VnoreneMenu.add_command(label="Položka2",command=Soubor)
# # VnoreneMenu.add_command(label="Položka3",command=Soubor)

# HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)

# #zobrazení hlavního menu
# hlavni.config(menu=HorniMenu)

# mainloop()

"""
Úkol:
1) Vytvořte program ukázky jazyků s rozbalovacím menu
   o dvou položkách:

   Soubor
    - Anglicky
    - Německy
    - Španělsky
    - Konec
    
   Nápověda
    - O aplikaci
    - O autorovi
   
"""    
    
#1
import tkinter as tk
from tkinter import messagebox

okno = tk.Tk()
okno.title("Rozbalovací menu")

def zobraz_info(tema):
    if tema == "O aplikaci":
        messagebox.showinfo("O aplikaci", "Rozbalovací menu s jazyky.")
    elif tema == "O autorovi":
        messagebox.showinfo("O autorovi", "Ondřej Sika")

def vyber_akce(akce):
    if akce == "Anglicky":
        print("Angličtina")
    elif akce == "Německy":
        print("Německy")
    elif akce == "Španělsky":
        print("Španělština")
    elif akce == "Konec":
        okno.destroy()


menu = tk.Menu(okno)
okno.config(menu=menu)

soubor_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Soubor", menu=soubor_menu)

soubor_menu.add_command(label="Anglicky", command=lambda: vyber_akce("Anglicky"))
soubor_menu.add_command(label="Německy", command=lambda: vyber_akce("Německy"))
soubor_menu.add_command(label="Španělsky", command=lambda: vyber_akce("Španělsky"))

soubor_menu.add_separator()
soubor_menu.add_command(label="Konec", command=lambda: vyber_akce("Konec"))

napoveda_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Nápověda", menu=napoveda_menu)
napoveda_menu.add_command(label="O aplikaci", command=lambda: zobraz_info("O aplikaci"))
napoveda_menu.add_command(label="O autorovi", command=lambda: zobraz_info("O autorovi"))

okno.mainloop()


