# -*- coding: utf-8 -*-
"""
Created on Wed Feb 29 07:56:55 2012

@author: Martin
"""
"""
Výjimky
- slouží k zachycení chyb a problémových stavů
try:
    blok s kódem, kde může nastat chyba
except:
    blok, který se provede při chybě
else:
    nepovinný blok, který se provede, když nenastane
    chyba    
"""

# import math

# cislo=-10
# try:
#     odmocnina=math.sqrt(cislo)
#     print("Odmocnina z",cislo,"je",odmocnina)
# except:
#     print("Chyba, odmocnit lze jen nezáporná čísla!")    


# x=8
# y=0
# try:
#     print ("Pokus o výpočet podílu")
#     vysledek=x/y
#     print (vysledek)
# except:
#     print ("Nastala chyba deleni")
# else:    
#     print ("Deleni probehlo v poradku.")



# import math
# vstup=False
# while (vstup==False):
#     try:
#         cislo=float(input("Zadej cislo:"))
#         odmoc=math.sqrt(cislo)
#         print(odmoc)
#     except:
#         print("Zadávejte pouze kladná čísla!!!")
#     else:    
#         vstup=True


# try:
#     raise ZeroDivisionError
# except IOError:
#     print ("Chyba vstupu nebo vystupu")
# except ZeroDivisionError:
#     print ("Nastala chyba deleni nulou")
# except NameError:
#     print ("Chyba jmena ")
# except:
#     print ("Jina vyjimka")
# else:
#     print ("OK")

"""
Ukoly:
1) Ošetřete pomocí výjimky převod řetězce na číslo.
2) Spusťte v části try nějakou funkci a dejte jí
   špatný počet parametrů. 
3) Vytvořte si seznam o délce 3 a zkuste vypsat 
   4. prvek.
""" 


#1
# try:
#     vstupni_retezec = input("Zadejte číslo: ")
#     cislo = float(vstupni_retezec)
#     print("Zadané číslo:", cislo)

# except ValueError:
#     print("Chyba: Zadaný vstup není platné číslo.")

 #2
# def funkce(spravny_parametr):
#     print("Funkce byla spuštěna s parametrem:", spravny_parametr)

# try:
#     # Spuštění funkce s nesprávným počtem parametrů
#     funkce()  # Chyba, mělo by být funkce(spravny_parametr_hodnota)

# except TypeError as e:
#     print(f"Chyba: {e}")

 #3
seznam = [1, 2, 3]

try:
    print(seznam[3])
except IndexError:
    print("4. prvek neexistuje, seznam má jen", len(seznam), "prvky.")





