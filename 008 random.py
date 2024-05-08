# -*- coding: utf-8 -*-
"""
Generování náhodných čísel
---------------------------
V programech často potřebujeme získat náhodné číslo:
- počítač má vybrat z několika rovnocenných možností
  (třeba náhodné testové otázky, tahy hráče, házení
   kostkou, zamíchání karet)

Potřebujeme knihovnu random 
randint(od,do) - vygeneruje náhodné číslo z intervalu <od,do>
               - od a do musí být celá čísla, mohou být i záporná 
choice(data)   - vybere z dat náhodný prvek
               - data jsou obvykle řetězec nebo seznam
"""


import random


# x=random.randint(1,6)
# print ("Kostka hodila", x)

# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# print("Písmeno:", pismeno)


# kod=""
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# print(kod)


# test, zda měsíc má 31 dnů
# mesic = random.randint(1,12)
# print(mesic)
# if mesic in [1,3,5,7,8,10,12]:
#     print("Má 31 dnů.")
# else:    
#     print("Nemá 31 dnů.")


"""
Úkol:
1) Naprogramujte hru KÁMEN, NŮŽKY, PAPÍR.
   Hraje člověk proti počítači.

Vytvořte pomocné proměnné a používejte je místo čísel:
kamen=1
nuzky=2
papir=3

Náhled programu:
Hrajeme hru kámen, nůžky, papír
1) Kámen
2) Nůžky
3) Papír
Zadej svou volbu:
    
vyhodnocení + výpis + ošetření správného vstupu

"""
#1 Jedna možnost
print("Náhled do programu")
print("Hrajeme hru kámen, nůžky, papír")
print("1) Kámen")
print("2) Nůžky")
print("3) Papír")
uzivatel=int(input("Zadej svou volbu:"))
pocitac = random.randint(1,3)
if uzivatel == pocitac:
    print("remíza")
else:
    if uzivatel == 1 and pocitac == 2:
        print("Výhra")
    if uzivatel == 2 and pocitac ==3:
        print("Výhra")
    if uzivatel ==3 and pocitac == 1:
        print("Výhra") 
    else:
        print("Prohra")



#1 Druhá možnost
print("Náhled do programu")
print("Hrajeme hru kámen, nůžky, papír")
print("1) Kámen")
print("2) Nůžky")
print("3) Papír")
uzivatel=int(input("Zadej svou volbu:"))
pocitac = random.randint(1,3)
if uzivatel == pocitac:
    print("Remíza")
elif uzivatel == 1 and pocitac == 2 or uzivatel == 2 and pocitac == 3 or uzivatel == 3 and pocitac == 1:
    print("Výhra")
else:
    print("Prohra")
