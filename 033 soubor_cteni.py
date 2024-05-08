# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (čtení)
módy:
  "r" - otevře daný soubor pro čtení, soubor musí
        existovat
  "r+" - otevře existující soubor jak pro čtení, tak 
        pro zápis
                
readlines() - vrátí seznam řádků souboru od akt. poz.          
readline() - přečte řetězec od aktuální pozice do 
             konce řádku  
read(x) - přečte řetězec o zadané délce, když neuvedeme
          hodnotu, přečte celý soubor
        - při pokusu o čtení na konci souboru vrací
          prázdný řetězec ""
tell() - vrací aktuální pozici v souboru
seek(pocet) - posune aktuální pozici o daný počet
              bytů od začátku souboru

Užitečné textové funkce
splitlines() - jako split, oddělovačem je "\n"
"""


# soub=open("piskvorky.txt","r")
# seznam=soub.readlines()
# soub.close()
# print (seznam)


#Jak se zbavit konců řádků? Např. takto:
#for i in range(len(sez)):
#    sez[i]=sez[i][0:-1]
#print (sez)



# soubor=open("piskvorky.txt","r")
# for i in range(2):
#     soubor.readline()
# radek=soubor.readline()
# soubor.close()
# print(radek)


# soubor=open("piskvorky.txt","r")
# vsechno=soubor.read()
# print(vsechno)

# seznam = vsechno.splitlines()
# print(seznam)
# soubor.close()

#ukázka příkazu tell()
# soubor=open("piskvorky.txt","r")
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# text=soubor.read(10)
# print(text)
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# soubor.close()


#ukázka příkazu seek()
# soubor=open("piskvorky.txt","r")
# soubor.seek(4)
# text=soubor.readline()
# print(text)
# soubor.close()


#ošetření otvírání a práce s koncem souboru
# try:
#     soubor=open("jmena.txt","r")
#     radek=soubor.readline()
#     while radek!="":
#         print(radek)
#         radek=soubor.readline()
#     soubor.close()
# except:
#     print("Chyba při otvírání souboru!")


"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt. 
    Použijte buď readlines + writelines nebo read + write.
2) Přečtěte soubor PISMENA.TXT pomocí příkazu read(1) a 
   zjistěte, kolik je v něm písmen "a".
3) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   VSTUP.TXT:
   12 35\n
   43 71\n
   10 99\n
   ...
     
   Tento soubor postupně přečtěte a do souboru SOUCTY.TXT
   vypište řádkové součty ve formátu a+b=c.
   SOUCTY.TXT:
   12+35=47\n
   43+71=114\n
   10+99=109\n
   ...
   
4) Načtěte ze souboru řetězec o délce 10 znaků,
   který představuje datum a otestujte správnost 
   jeho formátu (dd.mm.rrrr). Jen formát, hodnoty čísel
   nemusí být pravdivé.
5) Načtěte od uživatele 5 řetězců do seznamu, ke každému
   přidejte \n a pomocí operace WRITELINES zapište seznam
   do souboru.
6) Pokuste se otevřít neexistující soubor v módu "a" a
   přidat na konec krátký text.
7) Otevřete nějaký soubor pro čtení a spočítejte, kolik má
   znaků. (Nápověda - přečtěte soubor jako jeden celý
   řetězec a zjistěte jeho délku)
8) V souboru neznámé délky jsou na řádcích údaje:
   věk - jméno
   věk - jméno
   ...
   Čtěte ze souboru data a zjistěte jméno nejstaršího člověka.
   Vypište jej na obrazovku. Můžete využít operaci split().
   Věk může být až trociferný.
"""



#1
# with open('pokus.txt', 'r') as input_file:
#     content = input_file.read()
# with open('kopie.txt', 'w') as output_file:
#     output_file.write(content)


#2
# with open('PISMENA.TXT', 'r') as file:
#     file_content = file.read()
#     count_a = file_content.lower().count('a')

# print("Počet písmen 'a' v souboru:", count_a)




#3
# import random

# pairs = [(random.randint(10, 99), random.randint(10, 99)) for _ in range(100)]
# with open('VSTUP.TXT', 'w') as file:
#     for pair in pairs:
#         file.write(f"{pair[0]} {pair[1]}\n")


#4
# # Nahrajeme řetězec ze souboru (předpokládejme, že soubor se jmenuje 'datum.txt')
# try:
#     with open('datum.txt', 'r') as file:
#         datum = file.read().strip()

#         # Rozdělíme řetězec na části podle teček
#         parts = datum.split('.')

#         # Otestujeme délku a typ částí
#         if len(parts) == 3 and all(part.isdigit() for part in parts):
#             day, month, year = map(int, parts)
            
#             # Otestujeme rozsah hodnot
#             if 1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999:
#                 print("Formát dat je správný.")
#             else:
#                 print("Formát dat není správný.")
#         else:
#             print("Formát dat není správný.")

# except FileNotFoundError:
#     print("Soubor s datem nenalezen.")
# except Exception as e:
#     print(f"Nastala chyba: {e}")

# Druhý u způsob #4

try:
    soubor = open("datum.txt", "r")
    vstup = soubor.read(10)
    soubor.close()

    vysledek = True
    if not vstup[:2].isdigit():
        vysledek = False
    if vstup[2] != ".":
        vysledek = False
    if vstup[3:5].isdigit():
        vysledek = False
    if vstup[5] != ".":
        vysledek = False
    if vstup[6:].isdigit():
        vysledek = False

    if vysledek == True:
        print("Datum odpovídá formátu")
    else:
        print("Datum neodpovídá formátu")

except:
    print("Nastaly potíže při čtení ze souborů")










#5
# # Načti od uživatele 5 řetězců do seznamu
# seznam_retezcu = []
# for i in range(5):
#     retezec = input(f"Zadej {i+1}. řetězec: ")
#     seznam_retezcu.append(retezec + '\n')

# # Zapiš seznam do souboru pomocí operace WRITELINES
# with open("vystupni_soubor.txt", 'w') as soubor:
#     soubor.writelines(seznam_retezcu)

# print("Data byla zapsána do souboru.")

#6
# try:
#     with open("neexistujici_soubor.txt", 'a') as file:
#         file.write("Toto je krátký text na konec souboru.")
# except FileNotFoundError:
#     print("Soubor nebyl nalezen.")
# except Exception as e:
#     print(f'Nastala chyba: {e}')



















import random as r
soubor = open("vstup.txt","w")
for i in range(100):
    a = r.randint(10, 99)
    b = r.randint(10, 99)
    vystup = "{} {}\n".format(a,b)
    soubor.write(vystup)
soubor.close()

vstup = open("vstup.txt","r")
vystup = open("soucty.txt","w")
radek = vstup.readline()
while radek != "":
    a = int(radek[:2])
    b = int(radek[3:5])
    c = a + b
    vystup.write("{}+{}={}\n".format(a,b,c))
    radek = vstup.readline()
vstup.close()    
vystup.close()


# soubor = open("lidi.txt")
# data = soubor.readlines()
# soubor.close()
# nej_vek = 0
# nej_jmeno = ""

# for radek in data:
#     dvojice = radek.split("-")
#     vek = int(dvojice[0])
#     jmeno = dvojice[1]
#     if vek > nej_vek:
#         nej_vek = vek
#         nej_jmeno = jmeno

# print(nej_vek, nej_jmeno)








