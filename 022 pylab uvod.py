# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:35:52 2012

@author: Martin
"""
"""
Materiály:
http://matplotlib.org/
"""    
"""
existuje fce triplot(x,y) - uzavře lomenou čáru
"""

# import pylab as p
# # x=[0,1,-1,3,4]
# # y=[5,2,1,2,-1]
# # p.plot(x,y)
# # p.show() #zobrazení grafu a anulování všech nastavení




# x=p.arange(-5,5,0.1) #vektor x od -5 do 5, krok 0.2
# # print(x)

# # x=p.linspace(-5,5,30) #vektor x od -5 do 5, 30 hodnot
# # print(x)

# y1=2*x+1
# y2=x**2
# y3=x**3

# p.grid() #zobrazení mřížky - funguje jako přepínač
# # p.grid(True) #zobrazení mřížky - nastaví vždy
# p.title("Graf funkce x3")
# p.xlabel("Osa x") # popis osy x
# p.ylabel("Osa y")

# p.plot(x,y1,label="$y=2x+1$") #vložení údajů do grafu
# p.plot(x,y2,label="$y=\sqrt{x^2}$") #syntaxe jazyka latex
# p.plot(x,y3,label="$y=x^3$")
# p.ylim(-1,10) #limity pro osu y
# p.xlim(-3,3)
# p.legend(loc="upper center") #zobrazení legendy umístění řetězcem nebo číslem 0-10
# p.show() #zobrazení grafu a anulování všech nastavení


"""
Úkol:
1) Zobrazte graf funkce y=1/x, kde x patří do <1,10>
2) Zobrazte graf funkce y=cos(x), interval  <0,4*p.pi>
3) Vypočítejte hodnoty funkce y1=2cos(3x)-1 a 
   přidejte ji do předešlého grafu
4) Vygenerujte si seznam 10-ti náhodných x-vých hodnot
   a obdobný seznam y-vých hodnot. Zobrazte graf. 
"""   

"""
Opakovací
1) Zobrazte graf funkce y=odmocnina(x), kde x patří do <0,1000>
"""

 #1
import pylab as p

# vytvoření pole x na intervalu <1,10> s krokem 0.1
x = p.arange(1, 10, 0.1)

# výpočet hodnot funkce y = 1/x pro každou hodnotu x
y = 1 / x

# vykreslení grafu
p.plot(x, y)

# nastavení popisků os
p.xlabel('x')
p.ylabel('y')

# zobrazení grafu
p.show()

# #2
# import pylab as p

# x = p.linspace(0, 4*p.pi, 100)
# y = p.cos(x)

# p.plot(x, y)
# p.show()

# #3
# import pylab as p
# import random

# x = p.linspace(0, 4*p.pi, 100)
# y = p.cos(x)
# y1 = 2*p.cos(3*x) - 1

# p.plot(x, y, label='cos(x)')
# p.plot(x, y1, label='2*cos(3*x)-1')
# p.legend()
# p.show()

#4
import pylab as p
import random
x = []
y = []
for i in range(10):
    x.append(random.randint(0,10))
    x.append(random.randint(0,10))
p.plot(x,y)
p.show()











