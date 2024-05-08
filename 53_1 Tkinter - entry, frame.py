# -*- coding: utf-8 -*-

# from tkinter import *


# hlavni = Tk()
# hlavni.title("Výpočet 2. mocniny")

# ramecek=Frame(hlavni, bd=1, relief="ridge")
# ramecek.pack()

# def vypocet():
#     x=int(vstup.get())
#     napis["text"]=x**2

# tlacitko=Button(ramecek, text="Druhá mocnina", command=vypocet)
# tlacitko.pack(side="left", padx=10, pady=10)

# napis=Label(ramecek,text="0",font=("Arial",50))
# napis.pack(side="left")

# vstup=Entry(ramecek, width=25)
# vstup.pack(side="left",padx=10, pady=10)

# hlavni.mainloop()
"""
Úkol:
1) Vložte do okna dva Framy pod sebe. V prvním budou vedle sebe
   Label s textem "Vstup:" a jedno Entry.
   Ve druhém bude Label "Výstup:" a ještě jeden Label pro 
   výstupní text. konec vložte tlačítko. Při jeho stisku se text z Entry 
   předá do výstupního Labelu.
    
2) Napište aplikaci, která bude obsahovat:
   - Label "Tajná šifra" - zvětšené písmo
   - Entry pro vstup textu
   - Tlačítko "Šifruj vstup"
   - Label pro výstup
   - Tlačítko "Konec"
   - vhodně použijte Frame
   
   Po stisku tlačítka se řetězec ze vstupu zašifruje 
   libovolnou metodou a výsledek se zobrazí v labelu.
"""    

#1
# import tkinter as tk

# def preved_do_vystupu():
#     vystupni_label.config(text=vstupni_entry.get())

# # Vytvoření hlavního okna
# root = tk.Tk()
# root.title("Převodník textu")

# # První Frame s vstupními prvky
# frame1 = tk.Frame(root)
# frame1.pack(pady=10)

# label_vstup = tk.Label(frame1, text="Vstup:")
# label_vstup.grid(row=0, column=0, padx=5)

# vstupni_entry = tk.Entry(frame1)
# vstupni_entry.grid(row=0, column=1, padx=5)

# # Druhý Frame s výstupním prvkem
# frame2 = tk.Frame(root)
# frame2.pack(pady=10)

# label_vystup = tk.Label(frame2, text="Výstup:")
# label_vystup.grid(row=0, column=0, padx=5)

# vystupni_label = tk.Label(frame2, text="")
# vystupni_label.grid(row=0, column=1, padx=5)

# # Tlačítko pro převod
# tlacitko_prevod = tk.Button(root, text="Převést", command=preved_do_vystupu)
# tlacitko_prevod.pack(pady=10)

# # Spuštění hlavní smyčky programu
# root.mainloop()



#2
import tkinter as tk
import random

class SifraAplikace:
    def __init__(self, master):
        self.master = master
        master.title("Šifrovací aplikace")

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.label_tajna_sifra = tk.Label(self.frame, text="Tajná šifra", font=("Arial", 16))
        self.label_tajna_sifra.pack()

        self.entry_text = tk.Entry(self.frame)
        self.entry_text.pack()

        self.button_sifruj = tk.Button(self.frame, text="Šifruj vstup", command=self.sifruj_text)
        self.button_sifruj.pack()

        self.label_vystup = tk.Label(self.frame, text="")
        self.label_vystup.pack()

        self.button_konec = tk.Button(self.frame, text="Konec", command=master.destroy)
        self.button_konec.pack()

    def sifruj_text(self):
        vstupni_text = self.entry_text.get()
        zasifrovany_text = self.sifruj_metodou(vstupni_text)
        self.label_vystup.config(text=zasifrovany_text)

    def sifruj_metodou(self, text):
        # Zde můžete implementovat libovolnou šifrovací metodu
        # Pro jednoduchost použijeme například posun o náhodné číslo
        posun = random.randint(1, 26)
        zasifrovany_text = ""

        for znak in text:
            if znak.isalpha():
                if znak.islower():
                    zasifrovany_text += chr((ord(znak) - ord('a') + posun) % 26 + ord('a'))
                else:
                    zasifrovany_text += chr((ord(znak) - ord('A') + posun) % 26 + ord('A'))
            else:
                zasifrovany_text += znak

        return zasifrovany_text

root = tk.Tk()
app = SifraAplikace(root)
root.mainloop()