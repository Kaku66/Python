# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 09:17:29 2011

@author: Radek
"""
"""
Cyklus for
----------
- jedná se o cyklus s řídící proměnnou
- dopředu je znám počet opakování
- nemůže nastat nekonečný cyklus

Princip
- řídící proměnná postupně nabývá všech hodnot z
  pevně dané množiny
- pro každou hodnotu se vykoná jedna iterace  

Pozn!
Fce range() pracuje pouze s celými čísly.
Lze použít i záporná čísla.


for i in [množina hodnot]:
    tělo cyklu
"""

# for i in 1,3,14,2,9,1000:
#     print (2*i)


# retezec="Olomouc"
# for i in retezec:
#     print (i)

 
# for i in range(15):     #[0,1,2,...,14]
#       print (i)

#pocatecni hodnota i=0
#krok=1
#koncova hodnota i=14


# for i in range(5,10):
#     print (i)
   
#pocatecni hodnota i=5
#krok=1
#koncova hodnota i=9

for i in range(100,10,-5):  #[100,95,80,...15]
    print (i)

#pocatecni hodnota i=100
#krok=-5
#koncova hodnota i=15

"""
Úkol:
1) Načtěte z klávesnice číslo x a vypište pod sebou x hvězdiček.
2) Vypište posloupnost čísel 52, 54, ..., 78.
3) Vypište náhodný počet (1-50) náhodných čísel (1-100).
4) Načtěte číslo a vypište všechny jeho celočíselné dělitele.
5) Zjistěte, zda zadané číslo je prvočíslo.
"""

import random
#1
set=int(input("Zadejte počet"))
for i in range (set):
    print("*")
#2
for i in range(52,80,2):
    print(1)

#3
pocet=random.randint(1,50)
for i in range(pocet):
    cisla=random.randint(1,100)
    print(cisla)

#4
cislo=int(input("Zadejte cislo"))
for i in range(1, cislo+1,1):
    y=cislo%i
    if y==0:
        print(i)

#5
pocet=0
cislo=int(input("Zadejte cislo"))
for i in range(2,cislo):
    y=cislo%i
    if y==0:
        pocet+=1
    if pocet>1:
        