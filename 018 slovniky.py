# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:48:08 2012

@author: Radek
"""
import random
DB={}
DB['Mirek']=['Mirek','Palackeho 16','Olomouc','732 675 810']
DB['Dana']=['Dana','Litovelska 7','Olomouc','775 321 405']
DB['Jana']=['Jana','Husova 7','Litovel','775 321 405']
DB['Pepa']=['Pepa','Komenskeho 9','Praha','845 207 536']
DB['Marek']=['Marek','Jarni','Olomouc','776 345 890']
DB['Michal']=['Michal','Mezice 20','Mezice','606 267 762']
DB['Petra']=['Petra','Neznama 34','Opava','731 456 789']

# print(DB)

jmeno=0
ulice=1
mesto=2
telefon=3

# print (DB["Jana"][3])
# print (DB["Jana"][telefon])


# for klic in DB:
#     print(DB[klic])

# Výpis všech jmen, jejichž telefon začíná 7
for klic in DB:
    if DB[klic][telefon][0]=="7":
        print (DB[klic][jmeno],"-",DB[klic][telefon])

      
"""
Úkoly:
0) Přidejte do DB 1 vlastní záznam, vypište všechny údaje    
1) Vypište seznamy údajů lidí z Olomouce
2) Všechna města Olomouc nahraďte v DB za Opavu   
3) Do každého záznamu přidejte náhodný věk 
   (15-25 let) jako 5. položku seznamu
4) Nechejte zadat uživatele jméno a pokuste se smazat záznam
   z databáze (rozlište IFem). 
"""










# jmeno = input("Zadej jméno pro smazání:")
# if jmeno in DB:
#    del DB[jmeno]
#    print(DB)
#    print("Záznam byl smazán")

# else:
#    print("Záznam není v databázi!")


for person in DB:
   if person["město"] == "Olomouc":
      print(person)

#1
for klic in DB:
   if DB[klic][mesto] == "Olomouc":
      print(DB[klic])


#2
for klic in DB:
   if DB[klic][mesto] == "Olomouc":
      DB[klic][mesto] == "Opava"

#3
for klic in DB:
   DB[klic].append(random.randint(15,25))
for klic in DB:
   print(DB[klic])

#4
jmeno = input("Zadejte jméno")
if jmeno in DB:
   del DB[jmeno]
   print("Kontakt byl smazán")
else:
   print("Nebyl nalezen")

for klic in DB:
   print(DB[klic])












