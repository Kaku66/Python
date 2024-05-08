# -*- coding: utf-8 -*-
"""
Formátovaný řetězec pomocí funkce format()
- do řetězce vkládáme pomocí indexů hodnoty
  z n-tice
- obecný tvar je:
  retězec="{index:specifikátor}".format(n-tice)

https://www.sallyx.org/sally/python/python3b.php#format3
https://docs.python.org/3/library/string.html#format-specification-mini-language
http://howto.py.cz/cap06.htm#17
"""
# d = 2
# m = 5
# r = 2023


# Méně vhodný způsob
# datum = str(d) + ". " + str(m) + ". "+ str(r)
# print(datum)

#hodnoty se dosadí do řetězce dle {indexů}
# ret = "Dnes je {0}. {1}. {2}".format(d,m,r)
# print(ret)

#indexy parametrů lze vynechat :)
# ret = "Dnes je {}. {}. {}".format(d,m,r)
# print(ret)

#hodnoty se dosadí do řetězce dle {indexů}
# ret = "Dnes je {0:2}. {1:02}. {2}".format(d,m,r)
# print(ret)



#vložení desetinného čísla (dochází k matemat. zaokr.)
# ret = "Číslo pí má hodnotu {0:8.3f}".format(123.14159)
# print(ret)

#lze vkládat i hodnoty z různých struktur
# seznam=["Chleba","stojí",28.50,"Kč"]
# ret="{0[0]} {0[1]} {0[2]:10.2f} {0[3]}".format(seznam)
# print(ret)

#pozor, u slovníků se nepíší uvozovky u klíče!!!

#lze uvádět různé soustavy celého čísla
# (b = binárně, x = hexadecimálně, c = znak)
# ret = "Číslo {0} je binárně {0:b}".format(2022)
# print(ret)
# ret = "Číslo {0} je hexadecimálně {0:x}".format(2022)
# print(ret)
# ret = "Znak s kódem {0} je znak {0:c}".format(64)
# print(ret)

#v rámci volného prostoru můžeme obsah zarovnávat nebo i 
#vyplnit nějakým znakem, automaticky se vyplňuje mezerami

# ret="Číslo {:<15} zarovnané doleva".format(28)
# print(ret)
# ret="Číslo {:0>15} zarovnané doprava".format(28)
# print(ret)
# ret="Číslo {:^15} zarovnané na střed".format(28)
# print(ret)
# ret="Číslo {:^15} zarovnané na střed".format(28)
# print(ret)


# ret = f"{d}. {m}. {r}"
# print(ret)

# ret = f"Zarovnané na střed {28:_^20} prostoru."
# print(ret)

"""
Úkol:
1) Vypište pod sebou 10 náhodných časových údajů ve 
   formátu hh.mm.ss.
2) Vložte číslo 42 4krát do řetězce. Desítkově, binárně, 
   hexadecimálně a jako znak. 
3) Vypište pod sebe 10 náhodných čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla ve sloupci byla zarovnána vlevo
      12   Kc
      897  Kc
      6    Kc
   b) čísla ve sloupci byla zarovnána vpravo     
        12 Kc
       897 Kc
         6 Kc
   Nápověda: Čísla si uložíme do seznamu.
"""
#1
# import random

# for _ in range(10):
#     hours = random.randint(0, 23)
#     minutes = random.randint(0, 59)
#     seconds = random.randint(0, 59)

#     time_str = f"{hours:02d}.{minutes:02d}.{seconds:02d}"
#     print(time_str)

#2
cislo = 42

# Desítkově
retezec_desitkove = str(cislo) * 4

# Binárně
retezec_binarne = bin(cislo)[2:] * 4

# Hexadecimálně
retezec_hexa = hex(cislo)[2:].upper() * 4

# Jako znak
retezec_znak = chr(cislo) * 4

print("Desítkově:", retezec_desitkove)
print("Binárně:", retezec_binarne)
print("Hexadecimálně:", retezec_hexa)
print("Jako znak:", retezec_znak)

# #3
# import random

# # Generování a výpis náhodných čísel zarovnaných vlevo
# print("Zarovnáno vlevo:")
# for _ in range(10):
#     number = random.randint(0, 1000)
#     print(f"{number:<5} Kc")

# # Generování a výpis náhodných čísel zarovnaných vpravo
# print("\nZarovnáno vpravo:")
# for _ in range(10):
#     number = random.randint(0, 1000)
#     print(f"{number:>5} Kc")
