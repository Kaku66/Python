# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:24:04 2011

@author: Radek
"""
"""
Už známe, protože je používáme.
Existují 2 druhy parametrů - poziční a pojmenované.

Výhody podprogramů:
    1) Přehlednost
    2) Opakované použití - ušetříme psaní
    
Syntaxe:
def Název (parametr1,parametr2,...):
    blok příkazů
    return výsledný výraz

Pozn. Pokud neuvedeme return, vrací se vždy None    

Počet parametrů:
    a) žádné            def Fce()
    b) konkrétní počet  def Fce(x,y,z)
    c) proměnlivý počet def Fce(x,*param)

Implicitní hodnoty parametrů:
    V definici funkce může být do parametru 
    předána implicitní hodnota, která se použije
    v případě, že tento parametr nebude dosazen.
   !Všechny parametry vpravo od něj, musí být také
    implicitní.
"""    

# def Pozdrav():
#     print ("Good morning!")

# # Pozdrav()


# def Pozdravy(pocet):
#     # print(pocet)
#     for i in range(pocet):
#         print ("Buenos dias!")

# # Pozdravy(3)
# # print(pocet)


# def SuperPozdrav(pocet,text):
#     for i in range(pocet):
#         print (text)

# # SuperPozdrav(5,'Guten Tag!')
# # SuperPozdrav(4,"Wan shang chao")


# def Mocnina1(x):
#     vysledek=x**2
#     return vysledek

# # print(Mocnina1(5))



# def Mocnina2():
#     vstup=int(input("Zadej číslo pro umocnění:")) #tohle by zde nemělo být 
#     na2=vstup**2
#     na3=vstup**3
    
#     return (na2, na3)
#     print("Ahoj") #toto se ignoruje

# vysledek = Mocnina2()
# print(vysledek)


# sez = [6,3,2]
# print(sez.sort())

"""
Úkol:
1) Napište podprogram AnaX(A,X), která bude mít dva parametry
   A a X a bude počítat a vypisovat hodnotu A na Xtou.
2) Napište podprogram Linear(a,b), která vypíše řešení lineární
   rovnice (ax+b=0). Má dva parametry a,b.     
3) Napište funkci Prumer(a,b,c), která vrátí (return) aritmetický
   průměr ze tří čísel.
4) Napište fci Kostka(), která vrátí hodnotu hodu kostkou.
5) Napište funkci VratSeznam(pocet, od, do), která vrátí
   seznam náh. čísel o daném počtu a rozsahu
6) Vytvořte fci ZasifrujText(txt), která vrátí zašifrovaný
   text tak, že mezi jeho písmena vloží náhodná písmena navíc.
"""

"""
Další:
1) Funkce PocetSamohlasek(txt), která vrátí počet samohlásek 
   ze vstupního parametru txt.
2) Funkce Presmycka(txt), která náhodně zamíchá znaky z původního
   textu a vrátí tuto přesmyčku.  
"""

"""
def PokusSParametry1(x,*par):
    print (x)
    print (par)
    print (par[0])


PokusSParametry1(1000,"jeden","dva","tri")
"""


"""
def PokusSParametry2(x=2,y,z):
    print (x)
    print (y)
    print (z)

PokusSParametry2(12,10)
"""

# def Pozdrav():
#     print("Good morning")

# #Pozdrav()

# def Pozdravy(pocet):
#     print(pocet)
#     for i in range(pocet):
#         print("Buenos dias")

# Pozdravy()

#1
# def AnaX(A, X):
#     vysledek = A ** X
#     print(vysledek)
# AnaX(2, 5)

# #2
# def Linear(a, b):
#     x = -b/a
#     print( x)

#3
def Prumer(a, b, c):
    return (a + b + c) / 3
prumer = Prumer(3, 4, 5)
print(prumer) # Vypíše 4.0

#4
import random

def Kostka():
    return random.randint(1, 6)

#5
import random

def VratSeznam(pocet, od, do):
    seznam = []
    for i in range(pocet):
        cislo = random.randint(od, do)
        seznam.append(cislo)
    return seznam
