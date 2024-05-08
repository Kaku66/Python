# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:59:50 2012

@author: Martin
"""
"""
Připojení knihovny
    1) import knihovna  -> knihovna.funkce()
    2) import knihovna as m -> m.funkce()
    3) from knihovna import * -> funkce() 
       - POZOR, může dojít k přepsání importovaných
       proměnných nebo fcí, pokud se v importovaných
       knihovnách jmenují stejně
"""

import math     #připojení knihovny math

# print ("Číslo pí: ", math.pi)
# print ("Eulerovo číslo: ", math.e)


# print ("Absolutní hodnota: ",abs(-67.5))
# print ("Odmocnina: ", math.sqrt(16))


# print ("Sinus 30°: ", math.sin(math.pi/180*30))
# print ("Cosinus 45°: ", math.cos(math.radians(45)))
# print ("Tangens 45°: ", math.tan(math.radians(45)))


# print ("Useknutí desetinné části: ", math.trunc(61.4788))
# print ("Zaokrouhlení nahoru: ", math.ceil(61.4788))
# print ("Zaokrouhlení dolů: ", math.floor(61.4788))
# print ("Zaokrouhlení: ", round(61.4788,2)) #není v math


# print ("Logaritmus: ", math.log(1024,2))

"""
Ukol:
1)Spočítejte odmocninu ze zlomku 8/3.     

2)Uživatel zadá 2 odvěsny v pravoúhlém trojúhelníku. 
  Spočítejte délku přepony.
  Výsledek zaokrouhlete na 1 des. místo.  
    
3)Díváte se na strom ze vzdálenosti 100m pod 
  úhlem 20°. Jak je vysoký?
  Výsledek zaokrouhlete směrem dolů na celé metry.
  (Mělo by vyjít 36m)
  
4)Upravte předchozí program tak, aby vzdálenost a 
  úhel mohl zadat uživatel z klávesnice.
"""       


#1
print("Odmocněte ze zlomku",math.sqrt(8/3))
#2
odvesna1=float(input("Zadej odvěsnu: "))
odvesna2=float(input("Zadej odvěsnu: "))
vypocet=math.sqrt((odvesna1**2)+(odvesna2**2))
prepona=round(vypocet,1)
print("Přepona:", prepona)

#3,4
uhel=int(input("Zadej úhel:"))
vzdalenost=int(input("Zadej vzdálenost:"))
vyska=vzdalenost*math.tan(math.radians(uhel))

print("Výška je",math.floor(vyska),"metrů")




