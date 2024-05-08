# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:44:14 2012

@author: Radek
"""

# from tkinter import * 

# hlavni = Tk()
# hlavni.geometry("200x150")
# hlavni.resizable(False,False)

# ramecek = Frame(hlavni)
# ramecek.pack()


# skupina=LabelFrame(ramecek,bd=2,text="Volba", relief="ridge")
# skupina.grid(row=0)

# v = IntVar() 
# v.set(2)

# def tisk():
#     print (v.get())
    
# r1=Radiobutton(skupina, text="Jedna", variable=v, value=1)
# r1.grid(row=0,sticky=W) 
# r2=Radiobutton(skupina, text="Dva", variable=v, value=2)
# r2.grid(row=1,sticky=W)
# r3=Radiobutton(skupina, text="Tri", variable=v, value=3) 
# r3.grid(row=2,sticky=W) 
    
# tlacitko=Button(ramecek,text="Kontrola",command=tisk)
# tlacitko.grid(row=1)
 
# mainloop() 

"""
1) Vytvořte skupinu tří radiobuttonů s různými pozdravy.
   Přidejte tlačítko 'Pozdrav'. Po jeho stisku se 
   zobrazí hláška s daným pozdravem (použijte showinfo).
"""   

#1
import tkinter as tk
from tkinter import messagebox

okno = tk.Tk()
okno.title("Pozdravní aplikace")

def zobraz_pozdrav():
    vybrany_pozdrav = pozdravy.get()
    if vybrany_pozdrav:
        messagebox.showinfo("Pozdrav", f"Vybraný pozdrav: {vybrany_pozdrav}")
    else:
        messagebox.showwarning("Chyba", "Prosím, vyberte pozdrav.")


# Vytvoření proměnné pro uložení vybraného pozdravu
pozdravy = tk.StringVar()

radio_pozdrav1 = tk.Radiobutton(okno, text="Dobrý den", variable=pozdravy, value="Dobrý den")
radio_pozdrav2 = tk.Radiobutton(okno, text="Ahoj", variable=pozdravy, value="Ahoj")
radio_pozdrav3 = tk.Radiobutton(okno, text="Dobré ráno", variable=pozdravy, value="Dobré ráno")

# Umístění radiobuttonů na okno
radio_pozdrav1.pack()
radio_pozdrav2.pack()
radio_pozdrav3.pack()

tlacitko_pozdrav = tk.Button(okno, text="Pozdrav", command=zobraz_pozdrav)
tlacitko_pozdrav.pack()

okno.mainloop()

