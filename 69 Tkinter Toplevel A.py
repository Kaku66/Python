# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:49 2013

@author: Radek
"""
"""
Množství otevřených oken je možno regulovat pomocí zašednutí 
tlačítka.
"""
# from tkinter import *

# hlavni=Tk()
# hlavni.minsize(300,150)
# hlavni.title("Hlavní okno")

# def ZavriOkno():
#     global okno
#     # okno.destroy()
#     tlac["state"]="normal"
    
# def ZobrazOkno():
#     global okno
#     okno=Toplevel()
#     okno.minsize(300,100)
#     okno.title("Vedlejší okno")
#     tlac["state"]="disabled"
#     okno.protocol("WM_DELETE_WINDOW",ZavriOkno)


#     tlZavriOkno=Button(okno,text="Zavři toto okno",command=ZavriOkno)
#     tlZavriOkno.pack()   
#     tlZavriAplikaci=Button(okno,text="Zavři celou aplikaci",command=hlavni.destroy)
#     tlZavriAplikaci.pack() 

    
# tlac = Button(hlavni, text="Zobraz podokno",command=ZobrazOkno)
# tlac.pack()

# mainloop()

"""
Úkoly:
1) Umožněte uživateli otevřít z hlavního okna 2 podokna. Jedno bude 
   zelené a druhé červené. Zajistěte, aby nešlo otevřít více než 1
   vedlejší okno od každého druhu.
"""


#1
import tkinter as tk

def vytvor_hlavni_okno():
    okno = tk.Tk()
    okno.title("Hlavní okno")
    okno.geometry("400x200")

    barvy_oken = [{"nazev": "Zelené", "barva": "green", "otevreno": False, "okno": None},
                  {"nazev": "Červené", "barva": "red", "otevreno": False, "okno": None}]

    def otevrit_okno(barva):
        if not barva["otevreno"]:
            barva["okno"] = tk.Toplevel(okno)
            barva["okno"].title(f"{barva["nazev"]} okno")
            barva["okno"].geometry("300x150")
            barva["okno"].configure(bg=barva["barva"])
            barva["okno"].protocol("WM_DELETE_WINDOW", lambda: zavrit_okno(barva))

            barva["otevreno"] = True

    def zavrit_okno(barva):
        barva["otevreno"] = False
        barva["okno"].destroy()

    menu = tk.Menu(okno)
    okno.config(menu=menu)
    submenu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Otevřít", menu=submenu)

    for barva in barvy_oken:
        submenu.add_command(label=f"{barva["nazev"]} okno", command=lambda b=barva: otevrit_okno(b))

    okno.mainloop()

vytvor_hlavni_okno()










