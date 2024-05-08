# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:59:59 2013

@author: Radek
"""

# from tkinter import *
# from tkinter import messagebox

# okno = Tk()

# group = LabelFrame(okno, text="Zadej kladné číslo", padx=10, pady=10)
# group.pack(padx=10, pady=10)

# def kontrola():
#     try:
#         cislo=int(w.get())
#         if cislo<0:
#             messagebox.showwarning("Výstraha","Pozor, číslo nesmí být záporné!")
#             w.delete(0,END)            
#         else:    
#             messagebox.showinfo("Informace","Číslo bylo v pořádku.")
#     except:
#         messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
#         w.delete(0,END)

# w = Entry(group)
# w.pack()
# b= Button(group,text="Kontrola",command=kontrola)
# b.pack(pady=10)

# mainloop()

"""
Napište aplikaci kalkulačka podle P:\stejskal\python\cvičení Tkinter
"""    



# import tkinter as tk
# from tkinter import ttk

# def calculate():
#     try:
#         num1 = int(entry_num1.get())
#         num2 = int(entry_num2.get())
#         operator = entry_operator.get()

#         if operator == '//':
#             result = num1 // num2
#         elif operator == '%':
#             result = num1 % num2
#         else:
#             result = eval(f"{num1} {operator} {num2}")

#         result_var.set(result)

#     except ValueError:
#         result_var.set("spatny vstup")

# root = tk.Tk()
# root.title("Celočíselná Kalkulačka")

# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0)

# # Vytvoření vstupních polí a popisků
# labels = ["Číslo 1:", "Číslo 2:", "Operátor:"]
# entry_num1 = ttk.Entry(frame)
# entry_num2 = ttk.Entry(frame)
# entry_operator = ttk.Entry(frame)
# entries = [entry_num1, entry_num2, entry_operator]

# for i in range(len(labels)):
#     label = ttk.Label(frame, text=labels[i])
#     label.grid(row=i, column=0, sticky="w")
#     entries[i].grid(row=i, column=1)

# # Vytvoření tlačítka a výsledkového pole
# button_calculate = ttk.Button(frame, text="Spočítat", command=calculate)
# button_calculate.grid(row=0, column=2, rowspan=len(labels))
# label_result = ttk.Label(frame, text="Výsledek:")
# label_result.grid(row=0, column=3, sticky="w")
# result_var = tk.StringVar()
# entry_result = ttk.Entry(frame, state="readonly", textvariable=result_var)
# entry_result.grid(row=0, column=4)

# root.mainloop()



from tkinter import *

hlavni = Tk()
hlavni.title("Kalkulačka")

vysledne_cislo=StringVar()

# hlavní rámeček
nadpis=Frame(hlavni, relief="ridge")
nadpis.pack()

# každý frame pro jeden řádek
radek_1=Frame(hlavni, relief="ridge")
radek_1.pack()

radek_2=Frame(hlavni, relief="ridge")
radek_2.pack()

radek_3=Frame(hlavni, relief="ridge")
radek_3.pack()

radek_4=Frame(hlavni, relief="ridge")
radek_4.pack()

# def pro definování operací
def plus():
    x=int(vstup_x.get())
    y=int(vstup_y.get())
    vysledne_cislo.set(str(x+y))

def minus():
    x=int(vstup_x.get())
    y=int(vstup_y.get())
    vysledek.set(str(x-y))

def krat():
    x=int(vstup_x.get())
    y=int(vstup_y.get())
    vysledek.set(str(x*y))

def deleni_1():
    x=int(vstup_x.get())
    y=int(vstup_y.get())
    vysledek.set(str(x//y))

def deleni_2():
    x=int(vstup_x.get())
    y=int(vstup_y.get())
    vysledek.set(str(x%y))

# nadpis v rámečku nadpis
text_nadpisu=Label(nadpis,text="Kalkulačka",font=("Arial",20))
text_nadpisu.pack(side="left")

# text číslo a Entry pro zápis na 1. řádku
text_cislo_1=Label(radek_1,text="1. Číslo",font=("Arial",20))
text_cislo_1.pack(side="left")
vstup_x=Entry(radek_1, width=25)
vstup_x.pack(side="left",padx=10, pady=10)

# text číslo a Entry pro zápis na 2. řádku
text_cislo_2=Label(radek_2,text="2. Číslo",font=("Arial",20))
text_cislo_2.pack(side="left")
vstup_y=Entry(radek_2, width=25)
vstup_y.pack(side="left",padx=10, pady=10)

#tlačítka v řádku č. 3
tlacitko=Button(radek_3, text="+", command=plus)
tlacitko.pack(side="left", width=10)

tlacitko=Button(radek_3, text="-", command=minus)
tlacitko.pack(side="left", width=10)

tlacitko=Button(radek_3, text="*", command=krat)
tlacitko.pack(side="left", width=10)

tlacitko=Button(radek_3, text="//", command=deleni_1)
tlacitko.pack(side="left", width=10)

tlacitko=Button(radek_3, text="%", command=deleni_2)
tlacitko.pack(side="left", width=10)

# text výsledku a výstupní text na 4. řádku
text_vysledek=Label(radek_4,text="Výsledek ",font=("Arial",20))
text_vysledek.pack(side="left")
vysledek=Entry(radek_4,textvariable=vysledne_cislo, state="readonly")
vysledek.pack()

hlavni.mainloop()