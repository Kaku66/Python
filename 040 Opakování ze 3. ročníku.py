# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:50:02 2014

@author: Radek
"""

"""
Opakovací úkoly:
1) Načtěte z klávesnice délku řádku a
   vypište pomocí cyklu FOR hvězdičky
   dle vzoru.
   Př:
   Zadej číslo: 6
   6: ******     

2) Načtěte počet řádků a vypište diagram
   z náhodně dlouhých řádků.
   Př:
   Zadej počet řádků: 3
   2: **
   7: *******
   4: ****    

3) Načítejte postupně řadu čísel ukončenou
   hodnotou -1. Čísla budou vždy minimálně
   dvě a budou zadána korektně. Použijte 
   cyklus WHILE. Vypište 2. nejmenší číslo
   z řady.
    
4)Slovníky 
	Založte slovník ZBOZI a vypište jej: 
  {"chleb":30, "maslo":36, "mleko":17}
  Cyklem for zdražte ve slovníku všechno 
  zboží o 5 kč. 
  Cyklem vypište celý slovník takto:
    Slovník zboží:
    chleb: 35 Kc
    maslo: 41 Kc
    mleko: 22 Kc

5)Funkce
  Napište funkci GenerujHeslo(delka),
  která vrátí náhodné heslo dané délky.
  Heslo se může skládat z malých a velkých
  písmen a z číslic. 
  
  Př: GenerujHeslo(5) -> aB8xu

6)Graf
  Zobrazte graf funkce y=sin(3*x)-3*cos(x).
  Přidejte popisky os a název grafu.    
    
7)Formát řetězce
  Vygenerujte náhodnou registrační značku vozidla.
  Na první pozici nesmí být 0, ostatní číslice mohou
  nulu obsahovat. (např. 2M0 4012)

8)Seznamy
  Nadefinujte si seznamy A a B. Budeme je chápat
  jako množiny. Vytvořte seznam PRUNIK, který
  bude obsahovat průnik obou množin. Tedy všechny
  hodnoty, které se vyskytují jak v A tak v B.
  Seznam PRUNIK setříděte a vypište.

9) Soubory
Načtěte si obsah souboru "lide.txt". Na každém 
řádku je uvedeno toto: "jméno;příjmení;email".
Pomocí funkce split() si vytáhněte jednotlivé
části řádku a vytvořte z nich do výstupního 
souboru "lide.html" HTML tabulku.

10) Soubory
V souboru vstup.txt je na každém řádku několik
čísel oddělených mezerami. Počet není upřesněn.
Počet řádků též není upřesněn. Na každém řádku
je minimálně jedno číslo.
Vytvořte soubor vystup.txt, kde na každém řádku
bude součet hodnot ze stejného řádku ve vstupním
souboru.

"""


 #1
# delka=int(input("Zadej číslo:"))
# print(delka,":", end="")
# for i in range(delka):
#     print("*", end="")
# print()



#2
# import random

# # Načtení počtu řádků od uživatele
# pocet_radku = int(input("Zadej počet řádků: "))

# # Generování a výpis diagramu
# for i in range(pocet_radku):
#     delka = random.randint(1, 10)  # Náhodná délka řádku (1 až 10 hvězdiček)
#     hvezdicky = "*" * delka
#     print(str(delka) + ": " + hvezdicky)



#3
# # Inicializujeme proměnné pro nejmenší a druhé nejmenší číslo
# nejmensi = float("inf")
# druhe_nejmensi = float("inf")

# # Načítáme čísla od uživatele
# while True:
#     cislo = float(input("Zadejte cislo (-1 pro ukonceni): "))

#     if cislo == -1:
#         break  # Ukoncime nacitani cisel, pokud uzivatel zada -1

#     if cislo < nejmensi:
#         druhe_nejmensi = nejmensi  # Aktualizujeme druhe nejmensi cislo
#         nejmensi = cislo
#     elif cislo < druhe_nejmensi and cislo != nejmensi:
#         druhe_nejmensi = cislo  # Aktualizujeme druhe nejmensi cislo

# # Zkontrolujeme, zda bylo alespon dve cisla zadana
# if druhe_nejmensi == float("inf"):
#     print("Zadali jste mene nez dve cisla.")
# else:
#     print("Druhe nejmensi cislo je:", druhe_nejmensi)




#4
#   # Vytvoření slovníku ZBOZI
# zbozi = {"chleb": 30, "maslo": 36, "mleko": 17}

# # Cyklus pro zdražení zboží o 5 Kč
# for produkt, cena in zbozi.items():
#     zbozi[produkt] += 5

# # Výpis celého slovníku
# print("Slovník zboží:")
# for produkt, cena in zbozi.items():
#     print(produkt + ": " + str(cena) + " Kc")



#5
# import random

# def GenerujHeslo(delka):
#     malá_písmena = "abcdefghijklmnopqrstuvwxyz"
#     velká_písmena = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     číslice = "0123456789"
    
#     všechny_znaky = malá_písmena + velká_písmena + číslice
    
#     heslo = ""
    
#     for _ in range(delka):
#         náhodný_znak = random.choice(všechny_znaky)
#         heslo += náhodný_znak
    
#     return heslo

# # Příklad použití funkce s délkou hesla 5
# heslo = GenerujHeslo(5)
# print(heslo)


#6
import numpy as np
import matplotlib.pyplot as plt

# Generování hodnot x
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Generování hodnot y
y = np.sin(3*x) - 3*np.cos(x)

# Vytvoření grafu
fig, ax = plt.subplots()
ax.plot(x, y, label="Funkce: sin(3x) - 3cos(x)")

# Přidání názvu grafu a popisků os
ax.set_title('Graf funkce')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Přidání mřížky
ax.grid(True)

# Přidání legendy
ax.legend()

# Zobrazení grafu
plt.show()

#7
# import random

# def generuj_registracni_znacku():
#     # První pozice nesmí obsahovat 0, takže ji generujeme odděleně.
#     prvni_pozice = str(random.randint(1, 9))  # Generujeme náhodné číslo od 1 do 9.

#     # Generujeme zbylá čísla a písmena (celkem 6 znaků).
#     zbytek = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=6))

#     # Kombinujeme první pozici s zbytkem a vytvoříme registrační značku.
#     registracni_znacka = prvni_pozice + zbytek

#     return registracni_znacka

# # Volání funkce pro generování registrační značky.
# registacni_znacka = generuj_registracni_znacku()
# print(registacni_znacka)


# import random
# import string
# def GenerujRZ():
#     rz = str(random.randint(1,9))
#     rz += random.choice(string.ascii_uppercase)
#     rz += str(random.randint(0,9))
#     rz += " "
#     for i in range(4):
#         rz += str(random.randint(0,9))
#     return(rz)
   

#8
# Definice seznamů A a B
# A = [1, 2, 3, 4, 5]
# B = [3, 4, 5, 6, 7]

# # Vytvoření seznamu PRUNIK obsahujícího průnik obou množin
# PRUNIK = list(set(A) & set(B))

# # Setřídění seznamu PRUNIK
# PRUNIK.sort()

# # Výpis setříděného seznamu PRUNIK
# print(PRUNIK)