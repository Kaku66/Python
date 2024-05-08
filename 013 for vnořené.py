3# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:36:08 2013

@author: Radek
"""

"""
Vnořené cykly
"""

"""
sirka=int(input("Zadej šířku obdélníku:"))
vyska=int(input("Zadej výšku obdélníku:"))
for y in range(vyska):
    for x in range(sirka):
        print("* ",end="")
    print() 

#Napsat kód pro čtverec.
"""

      
"""
Úkol:
1) Vytvořte cyklus, který vypíše 6x dnešní datum.
   Celý cyklus zopakujte druhým cyklem 8x. 
    
2) Napište program, který 5x pod sebou vytiskne vaše 
   jméno (cyklem).
   Celý program zopakujte 30x (cyklem), vždy po 5-ti jménech
   vložte prázdný řádek.
   Napište před každé jméno jeho celkové pořadové číslo.
    
3) Vytvořte následující výpis pro libovolné n (toto bylo 4):
   1 : 1
   2 : 12 
   3 : 123
   4 : 1234

4) Načtěte n, vygenerujte n náhodných čísel a vypište
   ke každému z nich všechny jeho dělitele.
   Př: n=3
   4: 1 2 4
   18: 1 2 3 6 9 18
   11: 1 11
5) Vypište pyramidu z hvězdiček o výšce n.
   Př: n=4
      *
     ***
    *****
   ******* 
   Vytiskněte pod sebe několik náhodně velkých pyramid. Počet
   si zadá uživatel z klávesnice.
6) Zkuste vytisknout šachovnici 8x8 (nxn) ze dvou zvolených znaků:
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
   . @ . @ . @ . @
   @ . @ . @ . @ .
7) Máme řetězec "abcdefghijklmnopqrstuvwxyz". Načtěte z
   klávesnice počet hesel a vygenerujte z počátečního
   řetězce daný počet náhodných hesel délky 7 znaků.
"""


#1
# for y in range(8):
#     for x in range(7):
#         print("Dnešní nuda")

#2
# n=0
# for y in range(25):
#     for x in range(7):
#         n=n+1
#         print("Vaše jméno")
#     print(" ")

#3
# n=0
# x=int(input("Zadej pocet kolikrat"))

# for i in range(1,x+1):
#     print(x,":", n)

#4
# n=0
# x=int(input("Dělené číslo"))
# for i in range(x+1):
#     n=n+1
#     zbytek=x%n
#     zbytek==0:
#     print(n)

#5
# import random
# pocet =int(input("Zadej pocet pyramid:"))

# for i in range(pocet):
#    vyska = random.randint(3,10)
#    mezery = vyska - 1
#    hvezdy = 1

#    for y in range (vyska):
#       for x in range(mezery):
#          print(" ", end="")
#       for x in range(hvezdy):
#          print("*", end="")
#       print()
#       mezery -=1
#       hvezdy +=2

#6
velikost = int(input("ZADEJTE VELIKOST"))

for y in range(velikost):
   for x in range(velikost):
      print()
   for x in range(velikost):
      print("x@", end="")
   print()


#7
retezec = "abcdefghijklmnopqrstuvwxyz"
pocet_hesel = int(input("Zadejte pocet hesel:"))
for x in range(pocet_hesel):
   for y in "abcdefghijklmnopqrstuvwxyz":
      print(y)

