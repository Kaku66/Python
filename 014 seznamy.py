# -*- coding: utf-8 -*-
"""
                Seznamy
- uvádějí se v [], jednotlivé hodnoty se oddělují čárkou
- mohou obsahovat libovolná data i další seznamy
- čeština v seznamu?
"""

# seznam = [4,2,7]    #prázdný seznam
# print(seznam)    

# print(*seznam)    #print(4,2,7)

# for prvek in seznam:
#     print(prvek, end=" ")


seznam=[3,"Python",3.0,[1,0,1],False,1000]
print(seznam)

# print(seznam[1])
# print(seznam[1][1])

# seznam[2]="Programování" #přiřazení
# print(seznam)

    
# seznam=seznam+seznam #spojování seznamů
# print(seznam)

# seznam=[0]*10 #násobení seznamu konstantou
# print(seznam)

# import random
# seznam=[]
# for i in range(10):
#     seznam+=[random.randint(0,20)]
# print(seznam)


# seznam=list("Python")
# print(seznam)

# print(range(10,20))
# print(list(range(10,20)))

# print (seznam[4:]) #podseznam [4..n]
# print (seznam[1:4]) #podseznam [1..3]
# print (seznam[1:6:2]) #podseznam [1..5] každý 2. prvek

"""
Úkol:
1) Vytvořte 5-ti prvkový seznam obsahující nuly a 
   vypište jej.
   Pomocí cyklu načtěte 5 nových hodnot z klávesnice a 
   přepište nuly v seznamu těmito novými hodnotami.
   Seznam vypište.
   
2) Pomocí cyklu najděte v tomtéž seznamu nejmenší 
   prvek.
3) Zjistěte, jestli se v seznamu nachází hodnota 20.


Navíc:
4) Vytvořte si seznam 20ti náhodných čísel.
   Načtěte od uživatele hodnotu z klávesnice a zjistěte,
   kolikrát se daná hodnota nachází v seznamu. 
"""

#1
# sez = [0]*5  #Jinej zápis může být sez = [0,0,0,0,0]
# print(sez)
# for i in range(5):
#    cislo = int(input("Zadej číslo:"))
#    sez[i] = cislo
# print(sez)

#2
# sez = [0]*5
# print(sez)
# for i in range(5):
#    cislo = int(input("Zadejte číslo:"))
#    sez[i] = cislo
# print(sez)

# min = sez[0]  #Nastavuje minimum jako první prvek  v seznamu
# for i in sez:
#    if i < min:
#       min = i
# print(min)


#3
# sez = [0]*5
# print(sez)
# for i in range(5):
#    cislo = int(input("Zadejte číslo:"))
#    sez[i] = cislo
# print(sez)

# min = sez[0]
# for i in sez:
#    if i < min:
#       min = 1
# print("Minimum:", min)
