# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:49:39 2011

@author: Radek
"""
"""
Logické operátory dle priority
not - negace (unární)
and - logický součin (binární)
or  - logický součet (binární)

Priorita je stejná jako u aritmetických operací.
"""

# slovo=input("Zadej slovo: ")
# if not slovo=="Python":
#         print("Nezadal jsi Python!")

# if slovo!="Python":
#         print("Nezadal jsi Python!")

"""
rok = int(input("Zadej rok:"))
if rok>=2000 and rok<=2099:
    print ("Rok patří do 21. století")
else:
    print ("Rok nepatří do 21. století")
"""

"""
Úkol:
1) Načtěte strany trojuhelniku a zjistete, zda lze
   sestrojit.
2) Navic zjistete, jestli je pravouhly. Např. a=3,b=4,c=5. 
3) Načtěte souřadnice bodu (x,y) a rozhodněte, ve 
   kterém kvadrantu bod leží, či zda je na ose.
4) Načtěte rok a zjistěte, zda je přestupný. 
   (jsou to roky dělitelné 4, roky dělitelné 100 nejsou 
   přestupné, roky dělitelné 400 přestupné jsou)
   2022 není
   2024 je
   2100 není
   2000 je
""" 
  
"""
#1,2
a=int(input("Zadejte stranu a:"))
b=int(input("Zadejte stranu b:"))
c=int(input("Zadejte stranu c:"))
if a<b+c and b<a+c and c<b+a:
   print("Trojuhelník můžeme sestrojit")
else:
   print("Trojuhelník nejde sestrojit")
if c**2==a**2+b**2 or b**2==a**2+c**2 or a**2==b**2+c**2:
   print("trojuhelník je pravoúhlý")
else:
   print("Trojuhelník není pravoúhlý")
"""

"""
#3
x=int(input("Zadejte hodnotu x:"))
y=int(input("Zadejte hodnotu y:"))
if x<0 and y<0:
    print("bod leži ve čtvrtém kvadrantu")
elif x>0 and y>0:
    print("Bod leží v prvním kvadrantu")
elif x>0 and y<0:
    print("bod leži ve třetím kvadrantu")
else:
    print("bod leži ve drushém kvadrantu")
"""

#4
a=int(input("Zadejte rok:"))
if a%4 == 0 and not a%100 == 0 or a%400 == 0:
    print("Je přestupný")
else:
    print("Není přestupný")



