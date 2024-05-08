# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:44:08 2012

@author: Martin
"""
"""
text (x,y,řetězec) 
     - umístí řetězec na zvolené souřadnice v grafu
     - automaticky se vkládá nad y a vpravo od x, ale způsob
       zarovnání můžeme změnit pomocí nepovinných parametrů

annotate (řetězec,xy=(x,y),xytext=(x,y),arrowprops=dict(facecolor=color,shrink=x))
     - poznámka s šipkou
     - šipka ukazuje od poznámky na bod xy
     - poznámka je umístěna na souřadnicích xytext
     - vlastnosti šipky se definují v arrowprops, shrink znamená zkrácení
       šipky v obou směrech, uvádí se jako desetinné číslo (0.25 = čtvrtina)
"""

# import numpy as np
# import matplotlib.pyplot as plt

# x=np.arange(-2,3,0.01)
# y1=x**2-1
# y2=2*x+1
# plt.fill_between(x,y1,y2,where=(y2>y1), facecolor="gray")
# plt.plot(x,y1,"black")
# plt.plot(x,y2,"black")
# plt.text(0,0,"Popisek",fontsize="14", color="blue")
# #horizontalalignment="right",verticalalignment="center",color="r")

# plt.annotate("Vybarvená plocha", xy=(1,2), xytext=(1.5,-2), 
#           arrowprops=dict(facecolor="red"))
# plt.grid(True) 
# plt.show()


"""
Úkol:
1) Nakreslete funkci y1=-(x-2)^2 + 4.
   Vykreslete přímku y2=x čárkovanou čarou.
   Vybarvěte plochu mezi oběma čarami tam, kde platí
   že (y1>y2).
   Doplňte šipku s popisem směřující přibližně na střed
   vybarvené plochy.
   Pojmenujte průsečíky čar písmeny A a B.
   Přidejte legendu s popisem obou čar.

Opakovací:
1) Vykreslete funkce y1=|sin(x)| a y2=-|sin(x)| na 
   intervalu <0,4*pi>.
   Vybarvěte plochu mezi oběma čarami světle modrou 
   barvou tam, kde platí, že (x<2*pi).
   Přidejte legendu.
   Přidejte 2 popisky se šipkou. Jeden bude patřit k
   vyplněné oblasti a druhý k nevyplněné.
2) Najděte si na internetu funkci pro vykreslení srdce
   a zkuste zobrazit její graf.
     
"""    


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 6, 100)

# vykreslí se  y1 a y2 na stejném grafu
plt.plot(x, -(x - 2)**2 + 4, label="y1 = -(x-2)^2 + 4")
plt.plot(x, x, linestyle="--", label="y2 = x")

# označí se  průsečíky čar
A = (0, 0)
B = (3, 3)

plt.plot(A[0], A[1], marker="o", color="red", label="A")
plt.plot(B[0], B[1], marker="o", color="blue", label="B")
plt.text(-0.2,0.5, "A", fontsize="12" , color = "black")
plt.text(3,4.5, "B", fontsize="12" , color = "black")
plt.grid()


# vybarví se plocha mezi oběma čarami
x_fill = np.linspace(A[0], B[0], 100)
y_fill = -(x_fill - 2)**2 + 4
plt.fill_between(x_fill, y_fill, x_fill, where=(y_fill>x_fill), alpha=0.5)

# přidá šipku, která ukazuje na střed vybarvené plochy
center_x = (A[0] + B[0])/2
center_y = (A[1] + B[1])/2
plt.annotate("Střed plochy", 
             xytext=(center_x - 0.5, center_y - 3),
             xy=(center_x, center_y),
             arrowprops=dict(facecolor="black", shrink=1))

plt.legend()

plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 4 * np.pi, 1000)
# y1 = np.abs(np.sin(x))
# y2 = -np.abs(np.sin(x))

# plt.fill_between(x, y1, y2, where=(x < 2 * np.pi), color="lightblue")
# plt.plot(x, y1, label="y1 = |sin(x)|")
# plt.plot(x, y2, label="y2 = -|sin(x)|")

# arrow_props_filled = dict(facecolor="black", arrowstyle="->""")
# arrow_props_unfilled = dict(facecolor="white", edgecolor="black", arrowstyle="->""")

# plt.annotate("Prázdná oblast", xy=(3.5, 0.75), xytext=(3.5, 0.2), arrowprops=arrow_props_unfilled)
# plt.annotate("Vyplněná oblast", xy=(0.8, -0.75), xytext=(0.8, -0.2), arrowprops=arrow_props_filled)

# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Graphs  y1 a y2")
# plt.grid(True)
# plt.show()

# t = np.linspace(0, 2*np.pi, 1000)
# x = 16*np.sin(t)**3
# y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)


# #Srdce
# plt.plot(x, y, color="red")
# plt.axis("equal")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Graf funkce srdce")

# plt.show()



#Objem koule

# import math

# def vypocet_objemu_koule(polomer):
#     objem = (4/3) * math.pi * polomer**3
#     return objem

# polomer_koule = float(input("Zadej poloměr koule: "))
# objem_koule = vypocet_objemu_koule(polomer_koule)
# print("Objem koule je:", objem_koule)


# #Povrch koule
# import math

# def vypocet_povrchu_koule(polomer):
#     povrch = 4 * math.pi * polomer**2
#     return povrch

# # Zadejte poloměr koule
# polomer_koule = float(input("Zadejte poloměr koule: "))

# # Volání funkce pro výpočet povrchu koule
# povrch_koule = vypocet_povrchu_koule(polomer_koule)

# # Výpis výsledku
# print("Povrch koule je:", povrch_koule)



# #Objem válce
# import math
# def vypocet_objemu_valce(polomer, vyska):
#     if polomer <= 0 or vyska <= 0:
#         return "Poloměr a výška válce musí být kladné hodnoty."
#     else:
#         objem = math.pi * polomer**2 * vyska
#         return objem

# # Testování funkce
# polomer = float(input("Zadej poloměr válce: "))
# vyska = float(input("Zadej výšku válce: "))

# objem_valce = vypocet_objemu_valce(polomer, vyska)
# print("Objem válce je:", objem_valce)


#Povrch válce
import math
def vypocti_povrch_valce(polomer, vyska):
    
    # Výpočet povrchu válce
    podstava = math.pi * polomer**2
    plati = 2 * math.pi * polomer * vyska

    povrch = 2 * podstava + plati
    return povrch

# Příklad použití funkce
polomer = float(input("Zadej poloměr válce: "))
vyska = float(input("Zadej výšku válce: "))

povrch_valce = vypocti_povrch_valce(polomer, vyska)
print("Povrch válce je:", povrch_valce)

