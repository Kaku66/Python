# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 11:31:49 2013

@author: Radek
"""
"""
Komponenta Text
---------------
metoda tag_config(název, font=, foreground=, underline=)
- definice stylu

metoda insert(řádek.pozice, řetězec, styl)
- vkládá do textového pole řetězec na zadaný řádek od dané pozice
- ano, tyto dva údaje se oddělují tečkou
- pokud daná pozice neexistuje, vkládá na konec textu
- vložený text je formátován zvoleným stylem

metoda get(od, do)
- získání řetězce z komponenty text

metoda delete(od, do)
- smázání vymezené části textu
"""

# from tkinter import *

# hlavni=Tk()
# text=Text(hlavni)
# text.pack(fill=BOTH, expand=1)

# text.tag_config("modry", font="Arial 20 italic", foreground="blue", underline=1)
# text.tag_config("cerveny", font="Arial 15 bold", foreground="red", underline=0)

# text.insert(1.0,"Ahoj studenti!\n","modry")
# text.insert(5.0, "Jak se máte?\n","cerveny")
# text.insert(END, "To je dnes hezky...")



# smazat=Button(hlavni,text="Smazat vše", command=lambda: text.delete(1.0, END))
# smazat.pack()

# retezec=text.get(1.0, END)
# print (retezec)

# mainloop() 

"""
Úkol:
1) Vytvořte jednoduchý textový editor, který umožní
   uložit nebo načíst obsah komponenty text ze souboru.
   Tyto volby umožněte vybrat pomocí menu.
   Vše bez formátování = bez použití stylů.
   Použijte souborové dialogy.
   
   POZOR!
   - při stornování souborového dialogu nesmím nic otvírat
   - při otevření dalšího souboru musí předchozí obsah okna zmizet
"""    


#1
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Textový editor")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt"), ("Všechny soubory", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))

text_area = tk.Text(root, wrap="word")
text_area.pack(expand="yes", fill="both")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Soubor", menu=file_menu)

file_menu.add_command(label="Otevřít", command=open_file)
file_menu.add_command(label="Uložit", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Konec", command=root.destroy)

root.mainloop()










