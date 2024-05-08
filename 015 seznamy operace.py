# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 @author: Radek
"""
"""
        Seznamy a jejich operace
append(hodnota)       - přidá hodnotu na konec seznamu
count(hodnota)        - zjistí počet výskytů dané hodnoty
insert(index, hodnota)- vloží hodnotu na pozici v seznamu
pop(index)            - odebere prvek z dané pozice
remove(hodnota)       - odebere první výskyt této hodnoty
sort()                - setřídí seznam podle velikosti vzestupně
sort(reverse = True)  - setřídí seznam podle velikosti sestupně

delka=len(seznam)     - zjištění velikosti seznamu
copy()                - vrátí kopii seznamu (ne referenci)
""" 

seznam=[100,2023,1000,3,1,500,17]
# seznam=seznam+[2023]
seznam.append(2023) 
# print (seznam)


# print ("Pocet 2023: ",seznam.count(2023))

# seznam.insert(0,"Vlozeno") #vloží hod. na začátek
# print (seznam)


# # #Pokud neuvedeme index, odebírá z konce seznamu
# x=seznam.pop(0) #Odebere prvek z pozice 0
# print (x)
# print (seznam)


# seznam.remove(2023) #Odebere první výskyt
# print (seznam)


# seznam.sort(reverse=True)
# print (seznam)


# ret=["beta","c","a","alfa"]
# ret=["1000","10","20","100"]
# print(ret)
# ret.sort()
# print(ret)


# print(*ret)
# print("beta","c","a","alfa")


# sez1 = [1, 7, 9]
# sez2 = sez1
# sez1.append(50)
# print(sez1)
# print(sez2)


sez1 = [1, 7, 9]
# sez2 = sez1.copy()
# sez1.append(50)
# print(sez1)
# print(sez2)


# print ("Seznam má",len(sez1),"prvky.")

"""
Úkol:
1) Napište cyklus, který bude načítat z klávesnice 5 
   čísel a postupně je bude dávat na konec prázdného 
   seznamu. Seznam nakonec vypište.
2) Vygenerujte a vypište seznam 20-ti náhodných čísel.
3) Vygenerujte seznam 20-ti náh. čísel od 1 do 10,
   seznam setřiďte a vytvořte k němu seznam druhých
   mocnin. Oba seznamy vypište.
4) Zjistěte, kolikrát se v mocninách vyskytuje 81.
   Odstraňte všechna čísla 81 ze seznamu mocnin. 
5) Uložte do seznamu 6 náhodných hodů kostkou a zjistěte,
   jestli padla postupka tj. všechny hodnoty od 1 do 6.
6) Do seznamu "karty" vložte názvy karet. Vytvořte seznam
   "balicek" a vložte do něj zamíchané názvy karet.
   Help: karty=["♥7","♦7","♣7","♠7", ...]
7) Napište simuaci sportky. Člověk zadá 6 čísel, poté 
   počítač vylosuje také 6 čísel a vypíše, která čísla
   jsme uhádli. Čísla  musí být z intervalu 1-49. Čísla
   se nesmí opakovat.
"""


"""
DU) 
1) Naprogramujte jakoukoli hru s kostkami pro alespoň dva 
   hráče, jeden z nich bude počítač. 
2) Hra musí být dostatečně složitá a pro pro uchování hodů 
   bude používat seznamy. Příliš jednoduché hry budou vráceny
   k přepracování.
3) Musí být zobrazena pravidla.
4) Hra po spuštění zobrazí jednoduché textové menu:
   
   1) Zobraz pravidla
   2) Hrát hru
   3) Nastavení (nepovinná položka)
   4) Konec
   Zadej svou volbu:
       
   Po ukončení hry se program vrací do menu, nedojde k ukončení
   aplikace!
5) Hody hráčů (člověka i počítače) musí proběhnout až po stisku 
   klávesy Enter! 
   Použijte tento příkaz, který v podstatě způsobí čekání programu, 
   dokud uživatel nestiskne Enter: input("Stiskni Enter...").
   Snažte se o přehledné výpisy stavu hry - např. průběžné body
   za kolo a také celkové od začátku hry.
6) Každý musí mít jinou hru! :)   
""" 

import random
#1
sez = []
for i in range(5):
   cislo = int(input("Zadej číslo:"))
   seznam.append(cislo)
print(seznam)

#2
import random
seznam=[]
for i in range(20):
   cislo = random.randint(1,100)
   seznam.append(cislo)
print(seznam)


#3
# cisla = []
# for i in range(20):
#    cisla.append(random.randint(1,10))
# cisla.sort()
# print(cisla)
# mocniny = []
# for i in cisla:
#    mocniny.append(i**2)
# print(mocniny)

 #4
 #5
import random
seznam=[]
postupka=[1,2,3,4,5,6]
for i in range(6):
   cislo = random.randint(1,6)
   seznam.append(cislo)
print(seznam)
seznam.sort()
print(seznam)
if seznam==postupka:
   print("Padla postupka")
else:
   print("Nepadla postupka")
