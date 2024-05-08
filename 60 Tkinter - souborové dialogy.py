# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:21:47 2013

@author: Radek
"""
"""
Souborové dialogy
- musíme importovat filedialog
- slouží k získání cesty k souboru, nic neotvírají
- danou cestu musíme použít v příkazu open
- pozor, když dialog někdo stornuje, bude cesta prázdná ("")

dialog -> řetězec s cestou -> open(cesta,"mód")
"""
# from tkinter import filedialog
# from tkinter import *

# hlavni=Tk()
# hlavni.geometry("250x100")

# def Otevrit():
#     cesta = filedialog.askopenfilename(title="Otevřít soubor",filetypes=(('Python File', ('*.py','*.pyw')),('Text File', '*.txt'),('All Files', '*')))
#     print (cesta)
#     #zde proběhne otevření souboru pro čtení, čtení a uzavření
#     soubor=open(cesta,"r")
#     data=soubor.read()
#     soubor.close()
#     print(data)

    
# def Ulozit():
#     cesta = filedialog.asksaveasfilename(defaultextension='.txt',title="Uložit soubor", initialdir="P:\\")
#     print (cesta) 
#     #zde proběhne otevření pro zápis, zápis a uzavření
#     import random
#     soubor=open(cesta,"w")
#     for i in range(100):
#         soubor.write(str(random.randint(500,999))+"\n")
#     soubor.close()


# button1=Button(hlavni,text="Otevřít",command=Otevrit)
# button1.pack(pady=3) 
# button2=Button(hlavni,text="Uložit",command=Ulozit)
# button2.pack(pady=3) 
# mainloop()

"""
Úkol:
1) Vložte do okna jedno Entry a tlačítko Uložit. Uložte do 
   souboru text z Entry.
   Použijte dialog asksaveasfilename. 

"""   


#1
import tkinter as tk
from tkinter import filedialog


# Vytvoření hlavního okna
root = tk.Tk()
root.title("Uložit do souboru")

def ulozit_do_souboru():
    text = entry.get()

    if text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
                print(f"Text byl uložen do souboru: {file_path}")
        else:
            print("Ukládání bylo zrušeno.")
    else:
        print("Textové pole je prázdné. Nelze uložit do souboru.")


entry = tk.Entry(root, width=30)
entry.pack(pady=10)
ulozit_button = tk.Button(root, text="Uložit", command=ulozit_do_souboru)
ulozit_button.pack()
root.mainloop()


