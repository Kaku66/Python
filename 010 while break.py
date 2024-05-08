# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:54:17 2011

@author: Radek
"""
"""
continue - přeruší aktuální iteraci, cyklus 
           pokračuje další iterací
break - přeruší vykonávání cyklu
"""           

# while True:
#     heslo=input("Zadej vánoční kód:")
#     if heslo=="jedle":
#         break
#     print("Špatný kód, zadej znovu.")

# print("Spávný kód! Veselé Vánoce!")


# i=1
# while i<=10:
#     i+=1     
#     print("Kateřina")
#     continue
#     print("Mikuláš")




#co bude dělat tento cyklus a kdy skončí?

# import random
# x=1
# while x!=10:
#     x=random.randint(2,10)
#     if x%2==0:
#         continue
#     print (x)
#     if x==5:
#         break



""" 
Úkol:
1) Pomocí cyklu načítejte 5 čísel z klávesnice. Když bude 
   zadáno záporné číslo, použijte break. 
2) Naprogramujte hru myslím si číslo.
   Rozšíření: Vypsat počet pokusů.
3) Načtěte číslo a spočítejte jeho ciferný součet.
"""



#1
# x=0
# while x!=5:
#     x+=1
#     cislo=int(input("Zadej číslo:"))
#     if cislo < 0:
#         break


#2

# import random
# komp=random.randint(0,10)
# print(komp)
# pokus=1
# while True:
#     ty=int(input("Zadejte číslo prosím:"))
#     if komp < ty:
#         pokus=pokus+1
#         print("Zadej menší hodnotu")
#     if komp > ty:
#         pokus=pokus+1
#         print("Zadejte vyšší hodnotu")
#     if komp == ty:
#         print("Trefil jsi moje číslo")
#         print("Počet tvých blbostí:",pokus)
#         break


#3

user=int(input("Zadejte vámí zvolené číslo"))














