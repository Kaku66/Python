# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (textové)
open(cesta,mód) - otevře soubor a nastaví způsob
                  přístupu (mód)

módy:
  "r" - otevře daný soubor pro čtení, soubor musí
        existovat
  "r+" - otevře existující soubor jak pro čtení, tak 
        pro zápis
  "w" - otevře pro zápis, neexistující soubor bude
        vytvořen, existující soub. bude přepsán
  "a" - pro zápis na konec souboru, neexistující 
        bude vytvořen

close() - zavře soubor, způsobí uložení, uvolní jej
          pro jiné aplikace
flush() - vynucené uložení souboru
write() - zapíše do souboru daný řetězec na aktuální
          pozici
writelines() - zapíše do souboru seznam řádků         
  
"""

# data="Souborová data ze dne 27.9.2022"

# soubor=open("data.txt","w")  #systém se neptá a smaže!!!
# soubor.write(data)
# soubor.write("\n")
# soubor.write("Další data")
# soubor.close()



# soubor=open("data.txt","w")  
# x=0
# while x<1000000:         #pozor na nekonečný cyklus!!!
#     soubor.write(data)
#     x+=1
# soubor.close()



# import random
# soubor=open("cisla.txt","w")
# for i in range(100):
#     soubor.write(str(random.randint(1,1000))+"\n")
# soubor.close()


# seznam=["<html>\n","<head>\n","</head>\n","<body>\n","<h1>HTML stránka</h1>\n","</body>\n","</html>"]
# soubor=open("kostra.html","w")
# soubor.writelines(seznam)
# soubor.close()


# data2="\nData připojená na konec souboru"
# soubor=open("data.txt","a")
# soubor.write(data2)

# input("Stiskni Enter...")
# soubor.close()


"""
Úkoly:
1) Zapište do souboru CISLA.TXT pod sebe čísla od 1 
   do 1000.
   (Rozšíření: ka každému číslu doplnit jeho dělitele)

2) Načtěte z klávesnice celý název souboru, načtěte 
   řetězec a zapište jej do zadaného souboru.

3) Načtěte od uživatele 3 řetězce do seznamu a pomocí 
   operace WRITELINES zapište seznam do souboru.   

4) Zapište do souboru "heslo.dat" náhodné heslo 
   složené z číslic a velkých písmen o délce 7 znaků.
   
5) Do souboru tabulka.html vygenerujte html kód
   tabulky, která bude obsahovat odmocniny čísel od
   1 do 100.
   Bude mít dva sloupce, v řádcích bude vždy číslo a 
   odpovídající odmocnina zaokrouhlená na 2 místa.
"""   

   
#1
# # Otevření souboru CISLA.TXT v režimu zápisu (write)
# with open('CISLA.TXT', 'w') as file:
#     # Zápis čísel od 1 do 1000 pod sebe
#     for i in range(1, 1001):
#         file.write(str(i) + '\n')
        




# #2
# # Načtení názvu souboru z klávesnice
# nazev_souboru = input("Zadejte název souboru: ")

# # Načtení řetězce z klávesnice
# retezec = input("Zadejte řetězec, který chcete zapsat do souboru: ")

# # Zápis řetězce do souboru
# try:
#     with open(nazev_souboru, 'w') as soubor:
#         soubor.write(retezec)
#     print(f"Řetězec byl úspěšně zapsán do souboru {nazev_souboru}.")
# except:
#     print("Nastala chyba při zápisu do souboru.")



#3
# # Načti od uživatele 3 řetězce do seznamu
# retezce = []
# for i in range(3):
#     retezce.append(input(f'Zadej {i+1}. řetězec: '))

# # Zapiš seznam do souboru
# with open('output.txt', 'w') as soubor:
#     soubor.writelines(retezce)

# print('Data byla zapsána do souboru "output.txt".')

#4
# import random
# import string

# nove_heslo = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(7))

# with open("heslo.dat", "w") as soubor:
#     soubor.write(nove_heslo)

# print(f'Heslo bylo uloženo do souboru "heslo.dat".')

#5
import math
try:
    soubor = open("tabulka.html", "w")
    soubor.write('<table border="1")>\n')
    for i in range(1,101):
        radek = " "
        radek += "<tr> <td>"
        radek += str(i)
        radek += "</td> <td>"
        radek += str(round (math.sqrt(i),2))
        radek += "</td></tr>\n"
    soubor.write("</table>\n")
    soubor.close()
except:
    print("Došlo k chybě zápisu v souboru")