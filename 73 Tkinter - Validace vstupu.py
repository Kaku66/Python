# -*- coding: utf-8 -*-
"""
Validace vstupu
---------------
parametr validate
- říká, kdy se má volat validační funkce
- např. "key", "focusin", "focusout", "all"

parametr validatecommand
- tuto funkci volá hlavní okno a volá ji pokaždé, když
  nastane situace validate
- určuje validační funkci a její parametry
- parametry:
    %P - budoucí hodnota vstupu
    %d - při pokusu o vložení bude 1, při mazání bude 0, jinak -1
    %i - index, kam se bude vkládat nebo mazat
    %s - původní hodnota vstupu
    %S - vkládaný nebo mazaný text (Ctrl+V nebo delete)
    %W - jméno widgetu (komponenty)

funkce register
- aby hlavní okno mohlo volat validační funkci, musí
  ji mít zaregistrovanou  

odkazy:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html
https://www.geeksforgeeks.org/python-tkinter-validating-entry-widget/
"""
# from tkinter import *
# from tkinter import messagebox

# hlavni=Tk()
# hlavni.geometry("300x200")

# def test(hodnota,i,d):  #i,d
#     print("Index, kam se vkládá:",i)
#     print("Hodnota parametru d:",d)
    
#     if hodnota.isdigit() or hodnota == "":
#         return True
#     else:
#         return False    

# def test1(hodnota):
#     for i in hodnota:
#         if i not in "0123456789abcdefABCDEF":
#             return False
#     return True




# reg_fce1 = hlavni.register(test1)
# reg_fce = hlavni.register(test)

# nadpis = Label(hlavni, text = "Omezení vstupu", font=("Arial",18))
# nadpis.pack()
# popisek = Label(hlavni, text = "Vložte pokusný vstup:")
# popisek.pack()
# vstup=Entry(hlavni,validate="key",validatecommand=(reg_fce,"%P","%i","%d")) #,"%i","%d"
# vstup.pack()

# mainloop()

"""
Úkol:
1) Vložte do okna 3x Entry i s popisky a nastavte omezení vstupu:
   Entry1 - lze vkládat jen jedničky a nuly (musíme otestovat všechny
            znaky vstupu, nejen poslední vložený)
   Entry2 - lze vkládat jen hexačíslice (to samé)
   Entry3 - lze vkládat jen jen písmena  (řetezec.isalpha())  
"""


#1
import tkinter as tk

root = tk.Tk()
root.title("Vstupní pole s omezením")

def validate_entry1(char):
    return char in ["0", "1"]

def validate_entry2(char):
    return char.isdigit() or (char.lower() >= "a" and char.lower() <= "f")

def validate_entry3(char):
    return char.isalpha()

def validate_entry4(char, entry):
    if char == '.':
        return entry.count('.') == 0  # Pouze jedna tečka je povolena
    return char.isdigit() or char == '-'  # Desetinné číslo může obsahovat číslice a jednu pomlčku pro záporná čísla

def on_validate_entry1(char, entry):
    return validate_entry1(char) and all(validate_entry1(c) for c in entry.get())

def on_validate_entry2(char, entry):
    return validate_entry2(char) and all(validate_entry2(c) for c in entry.get())

def on_validate_entry3(char, entry):
    return validate_entry3(char) and all(validate_entry3(c) for c in entry.get())

def on_validate_entry4(char, entry):
    return True  # Povolit všechny znaky a všechny operace včetně mazání

entry1_label = tk.Label(root, text="Entry 1: Jedničky a nuly")
entry1_label.pack()
entry1_var = tk.StringVar()
entry1 = tk.Entry(root, textvariable=entry1_var, validate="key", validatecommand=(root.register(lambda char, entry=entry1_var: on_validate_entry1(char, entry)), '%S'))
entry1.pack()

entry2_label = tk.Label(root, text="Entry 2: Hexa cifry")
entry2_label.pack()
entry2_var = tk.StringVar()
entry2 = tk.Entry(root, textvariable=entry2_var, validate="key", validatecommand=(root.register(lambda char, entry=entry2_var: on_validate_entry2(char, entry)), '%S'))
entry2.pack()

entry3_label = tk.Label(root, text="Entry 3: Písmena")
entry3_label.pack()
entry3_var = tk.StringVar()
entry3 = tk.Entry(root, textvariable=entry3_var, validate="key", validatecommand=(root.register(lambda char, entry=entry3_var: on_validate_entry3(char, entry)), '%S'))
entry3.pack()

entry4_label = tk.Label(root, text="Entry 4: Desetinná čísla")
entry4_label.pack()
entry4_var = tk.StringVar()
entry4 = tk.Entry(root, textvariable=entry4_var, validate="key", validatecommand=(root.register(lambda char, entry=entry4_var: on_validate_entry4(char, entry)), '%S'))
entry4.pack()

root.mainloop()


























