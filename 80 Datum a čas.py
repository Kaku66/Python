# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:31:18 2013

@author: Radek
"""
"""
existuje i knihovna time
"""


# from datetime import *

# dnes = datetime.now()

# print (str(dnes))

# print (f"Aktualni rok: {dnes.year}")

# print (f"Aktualni mesic: {dnes.month}")
# print (f"Aktualni den: {dnes.day}")
# print (f"Aktualni hodina: {dnes.hour}")
# print (f"Aktualni minuta: {dnes.minute}")
# print (f"Aktualni vterina: {dnes.second}")
# print (f"Aktualni mikrosekunda: {dnes.microsecond}")

"""
Úkol:
1) Naprogramujte digitální hodiny, které 
   každou desetinu sekundy aktualizují svůj čas. 
   Zobrazujte pouze h:m:s. Využijte metodu after.
2) Zjistěte aktuální čas.
   Proveďte cyklus, který 1000 000x zvedne proměnnou
   o jedničku.
   Znovu zjistěte čas a vypište, jak dlouho cyklus 
   trval.
"""   

"""
cas1 = datetime.now()

x=1
for i in range(1000000):
   x+=1
   
cas2 = datetime.now()

cas = cas2 - cas1

print(cas.seconds)

"""




#1
import tkinter as tk
from datetime import datetime

def update_time(label):
    current_time = get_current_time(label)
    label.config(text=current_time)
    label.after(100, update_time, label)  # Aktualizace každých 100 ms

def get_current_time(label):
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time

root = tk.Tk()
root.title("Digitální hodiny")
root.geometry("200x100")

time_label = tk.Label(root, font=("Helvetica", 24))
time_label.pack(expand=True)

update_time(time_label)

root.mainloop()


#2
# import time

# # Zjistění aktuálního času před cyklem
# start_time = time.time()

# # Cyklus, který zvedne proměnnou 1000000x o jedničku
# promenna = 0
# for i in range(1000000):
#     promenna += 1

# # Znovu zjistění aktuálního času po provedení cyklu
# end_time = time.time()
# trvani = end_time - start_time
# print(f"Cyklus trval {trvani} sekund.")




























# from tkinter import *
# hlavni = Tk()

# hodiny=Label(hlavni,font=("Arial",100))
# hodiny.pack()

# def AktualizujCas():
#     ted=datetime.now()
#     vystup=f"{ted.hour:02}:{ted.minute:02}:{ted.second:02}"
#     hodiny["text"]=vystup
#     hlavni.after(1000,AktualizujCas)

# AktualizujCas()    

# mainloop()









