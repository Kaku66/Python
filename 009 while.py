# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011

@author: Radek
"""
"""
Cyklus while
- umožňuje opakované provádění příkazů

while PODMÍNKA:
    odsazené příkazy (blok)

Princip:
- dokud platí podmínka, bude se provádět blok
- podmínka má stejnou podobu jako u IFu
- POZOR, může nastat nekonečný cyklus!    

Možnosti přerušení nekonečného cyklu Spyder:
1) Kliknout do výstupního okna a stisknout Ctrl+c
2) Zavřít Spyder

Možnosti přerušení nekonečného cyklu VS Code:
1) Zavřít terminál
2) Správce aplikací -> VS Code -> Python -> ukončit úlohu

"""
"""
jmeno=input("Zadej jmeno: ")
i=1
while i<=10:
    print(jmeno)
   #  i+=1                #přičte hodnotu k proměnné i

print (i)
"""



#odhadněte, co bude dělat následující cyklus
#kdy skončí
#kolikrát proběhne

# import random
# x=1
# while x!=10:
#     x=random.randint(2,10)
#     print (x)


"""
Úkol:
1) Načítejte z klávesnice heslo, dokud nebude správně 
   zadáno. Správné heslo je "monitor".
2) Rozšíření úkolu 1). Zjistěte, na kolikátý pokus
   bylo heslo správně zadáno. 
3) Načtěte číslo n a sečtěte hodnoty od 1 do n
4) Vypište tabulku goniometrických funkcí pro úhly
   0 - 90° po 5-ti stupních. Pozor na nedefinované
   hodnoty. Čísla zaokrouhlete na 2 des. místa.
Výstup:
uhel  sin	cos	 tg	 cotg
0° 	0.0 	1.0    0.0 	 Inf.
5° 	0.09 	1.0    0.09  11.43
...
90°	1.0 	0.0    Inf.  0.0
   
""" 
"""
Navíc:
Načtěte od uživatele číslo a převeďte jej do
binární soustavy.    
"""

"""
#1,2
pokus=1
heslo=input("Zadejte heslo:")

if "lokotka"==heslo:
   print("Přihlášení proběhlo skvěle")
   print("Počet marných pokusů:", pokus)

while "lokotka"!=heslo:
   pokus+=1
   heslo=input("Zadejte znovu, protože jste zadali šparné heslo:")
   if "lokotka" ==heslo:
      print("Přihlášení proběhlo dobře!")
      print("počet pokusů:", pokus)
"""

#3
cislo=int(input("Zadej číslo: "))
cislo=1
pocet=1

   




