# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 08:32:40 2011

@author: Radek
"""


#Lepší způsob
# for i in "Olomouc":
#     print(i)


#Horší způsob

# ret="Olomouc"
# for i in range(len(ret)):
#     print (ret[i])


"""
Úkol:
1) Načtěte řetězec z klávesnice. Vytvořte z něj nový 
   řetězec tak, že za každé písmeno vložíte znak "*". 
   "Python" -> "P*y*t*h*o*n*"
2) Načtěte řetězec a spočítejte v něm písmena "a".  
3) Načtěte řetězec a spočítejte součet všech cifer, 
   které se v něm budou vyskytovat.
"""


vysledek=""
ret=input("Zadej retezec")
for i in ret:
   vysledek +=i+"*"
print(vysledek)


vstup= input("Zadejte text:")
soucet=0
for znak in vstup:
   if znak in "123456789":
      soucet += int(znak)
print("Soucet cifer ve vstupu:", soucet)    
    
    