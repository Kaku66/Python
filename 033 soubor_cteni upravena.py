# -*- coding: utf-8 -*-

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

# try:
#    soub=open("piskvorky.txt","r")
#    seznam=soub.readlines()
#    soub.close()
#    print (seznam)
# except:
#     print("Chyba při čtení ze souboru!")


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
#         print(radek,end="")
#         radek=soubor.readline()
#     soubor.close()
# except:
#     print("Chyba při otvírání souboru!")


"""
Úkoly:
1) Vytvořte si v Pozn. bloku soubor pokus.txt. Otevřete
   si jej v režimu pro čtení, přečtěte celý jeho obsah
   a vypište jej do souboru kopie.txt. 
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
5) V souboru lidi.txt neznámé délky jsou na řádcích 
   tyto údaje:
   věk - jméno
   věk - jméno
   ...
   Čtěte ze souboru data a zjistěte jméno nejstaršího člověka.
   Vypište jej na obrazovku. Můžete využít operaci split().
   Věk může být až trociferný.

Navíc:   
6) Pokuste se otevřít neexistující soubor v módu "a" a
   přidat na konec krátký text.
7) Otevřete nějaký soubor pro čtení a spočítejte, kolik má
   znaků. (Nápověda - přečtěte soubor jako jeden celý
   řetězec a zjistěte jeho délku)
"""





#5
with open("lidi.txt", "r") as file:
    data = file.readlines()
nejvyssi_vek = 0
for line in data:
    # Rozdělení řádku podle pomlčky
    vek, jmeno = line.split("-")
    
    # Převod věku na celé číslo a odstranění bílých znaků
    vek = int(vek.strip())
    
    if vek > nejvyssi_vek:
        nejvyssi_vek = vek
        nejstarsi_jmeno = jmeno.strip()
print(f"Nejstarší člověk je {nejstarsi_jmeno} s věkem {nejvyssi_vek} let.")

























