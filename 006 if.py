# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 08:35:56 2011

@author: Radek
"""
"""
Podmíněný příkaz (if) - umožňuje rozhodování
--------------------------------------------
if PODMÍNKA1:
    odsazené příkazy (blok1)
elif PODMÍNKA2:    
    odsazené příkazy (blok2)
elif ...
    ...    
else:
    odsazené příkazy (blokN)

Pozn. 
Části elif a else jsou nepovinné.
"""
"""
x=float(input("Zadej cislo:"))
if x>0: 
    print ("Cislo je kladne!")
    print ("Provedla se prvni vetev prikazu IF")
elif x==0:
    print ("Nula")
else:
    print ("Cislo je zaporne")
"""


# print(15<8)
   
"""
Relační operátory
>  větší   >= větší nebo rovno
<  menší   <= menší nebo rovno
== rovno   != nerovno

in testuje přítomnost prvku v množině
"""

# Testování intervalu
# x = 20
# if 5 < x < 15:
#     print("Platí")
# else:    
#     print("Neplatí")


# retezec="Python je programovací jazyk"
# if "program" in retezec:
#     print("Ano, je tam.")
# else:
#     print("Ne, není tam.")


"""
Úkol:
1) Načtěte z klávesnice 2 čísla a zjistěte, které z
   nich je větší, nebo jestli jsou stejná.
2) Načtěte celé číslo a zjistěte, zda je liché či sudé.
3) Načtěte řetězec (heslo) a zjistěte jestli je správné.
   Správné heslo je "klokan".
4) Načtěte koeficienty kvadratické rovnice, zjistěte
   kolik má řešení a vypište její řešení.  
   Testovací hodnoty:
   a = 1, b = -3, c = 2 -> x1 = 2, x2 = 1
   a = 1, b = -2, c = 1 -> x1 = 1
   a = 1, b = -2, c = 2 -> nemá řešení
"""   
"""
#1
x=int(input("Zadej první číslo:"))
y=int(input("Zadej druhé číslo:"))
if x>y:
    print("První číslo je větší")
elif y>x:
    print("Druhé číslo je větší")
elif x==y:
    print("Obě čísla jsou rovna")
"""

"""
#2
x=int(input("Zadej číslo:"))
zbytek=x%2
if x==0:
    print("číslo je nula")
elif zbytek==0:
    print("Číslo je sudé")
else:
    print("Číslo je liché")
"""

"""
#3
retezec=input("Zadej heslo:")
if "kokolíno" in retezec:
    print("Confirmed")
else:
    print("Špatné heslo")
"""
#4
import math


a=int(input("Zadej a:"))
b=int(input("Zadej b:"))
c=int(input("Zadej c:"))

D=b*b-4*a*c

if D>0:
    print("Rovnice má dva kořeny")
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
elif D==0:
    print("Rovnice ma jedno řešení")
    x=(-b+math.sqrt(D))/(2*a)
    print("X= ", x)
elif D<0:
    print("Rovnive není v R řešení")


"""
Textová hra Najdi poklad
Výpis:
Jsi v místnosti. Můžeš jít dál všemi 4-mi směry.
a) Jdi na sever
b) Jdi na jih
c) Jdi na západ
d) Jdi na východ
Zadej volbu:
Podle volby přejdeme do další místnosti, kde
nám hra nabídne další 3 směry.
Tam je pak buď poklad nebo něco jiného.
Poté program skončí.    

Texty použijte svoje např:
a) Tahle cesta nevede k pokladu.
b) Narazil jsi na strážce, který tě nepustil dál.
c) Našel jsi poklad!
d) Tato cesta vedla do prázdné místnosti.

    
Důležité:
Pokud uživatel zadá špatně vstup, program skončí a 
zobrazí se mu něco na tento způsob:
   
"Chyba vstupu, spusťte hru znovu!"    
"""















