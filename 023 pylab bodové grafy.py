# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:24:01 2012

@author: Martin
"""
"""
Styly barvy:
r - červená
g - zelená
y - žlutá

Styly čar:
-  plná
:  tečkovaná
-- čárkovaná

Styly vrcholů:
o kulaté body
^ trojúhelníčky
s čtverečky

Kombinace:
ro   - červená kolečka
bs:  - modré čtverečky a tečkovaná čára
g^-- - zelené trojúhelníky a čárkovaná čára
y-   - žlutá plná čára
""" 

# import pylab as p

# x=[1,2,3,4]
# y=[1,4,9,16]

# p.plot(x,y,"g:s") #použití formátovacího řetězce 'barvacaravrchol'
# # p.axis([0, 10, 0, 10]) #rozsah os x a y

# # p.plot(x,y,'ro') #vložení bodů do grafu 'barvatvar'

# # p.plot(x,y,color="green")
# # p.plot(x,y,'g--',color="#ff0000") #vložení bodů do grafu 'barvatvar'

# p.show()

"""
Úkol:
1) Vykreslete graf funkce y=x**3-2*x**2+x-1 jako 
   plnou čáru s kulatými vrcholy.
2) Vygenerujte seznam 20-ti náhod. bodů v rovině (0,20)
   a zobrazte jej pomocí čtverečků.   
3) Načtěte z klávesnice souřadnice tří bodů a zobrazte 
   trojúhelník. 
""" 


#1 
import pylab as p

# Vytvoření pole hodnot x
x = p.linspace(-5, 5, 40) 

# Výpočet odpovídajících hodnot y
y = x**3 - 2*x**2 + x - 1 

# Vykreslení grafu s kulatými vrcholy
p.plot(x, y, 'o-', markersize=4) # Vykreslení grafu s kulatými vrcholy

p.xlabel('x')
p.ylabel('y')
p.title('Graf funkce y=x**3-2*x**2+x-1')
# Zobrazení grafu
p.show() 

#2



  
