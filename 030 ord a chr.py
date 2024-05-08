# -*- coding: utf-8 -*-

"""
Převody znaků
Znakem se rozumí řetězec o délce 1.
ord() - převede znak na jeho ordinální hodnotu (číslo)
chr() - opačná funkce, získáme znak = jednoznakový řetězec
"""


# znak=input('Zadej znak: ')
# cislo=ord(znak)
# print(cislo)



# cislo=int(input('Zadej cislo znaku: '))
# znak=chr(cislo)
# print (znak)


"""
Ukol:
1) Vypište úsek ASCII tabulky od 50 do 100
2) Vypište abecedu z malých písmen do řádku.  
3) Vygenerujte a vypište náhodné Velké písmeno.
4) Načtěte slovo a vypište jeho znaky posunuté o 1.
5) Napište funkci, která vygeneruje náhodný řetězec z 
   libovolných malých písmen. Délka bude náhodná 
   mezi 10 a 1.

   
*) Rozšiřte předchozí funkci tak, aby se střídaly 
   souhlásky a samohlásky. Slovo začíná náhodně 
   samohláskou nebo souhláskou.
"""
#1
# for i in range(50, 101):
#     print(chr(i), end=' ')

# #2
# abeceda = "".join(chr(i) for i in range(ord("a"), ord("z")+1))
# print(abeceda)

# #3
# import random
# import string

# nahodne_velke_pismeno = random.choice(string.ascii_uppercase)
# print(nahodne_velke_pismeno)

# #4
# # Načtěte slovo od uživatele
# vstupni_slovo = input("Zadejte slovo: ")

# # Pro každý znak ve slově provede posun o 1
# posunute_slovo = ""
# for znak in vstupni_slovo:
#     posunuty_znak = chr(ord(znak) + 1)
#     posunute_slovo += posunuty_znak

# # Vypište výsledek
# print("Posunuté slovo:", posunute_slovo)

# #5
# import random
# import string

# delka = random.randint(1, 10)
# nahodny_retezec = ''.join(random.choice(string.ascii_lowercase) for _ in range(delka))
# print(nahodny_retezec)
