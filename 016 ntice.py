# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:17:39 2012

@author: Radek
"""

"""
N-tice (tuple)
- vytvářejí se pomocí ()
- jsou neměnné, obdobně jako řetězce
- nemají žádné metody (jako např. pop(),...)
- používají se pro uložení většího počtu hodnot než 1
"""

# ntice=()
# print (ntice)


# x = (7,'Ahoj',4.7,None,[4,5])
# print(x)
# x[4].append(6) 
# print(x)
# x[0] = 10


# a=b=c=1
# ntice=(a,b,c)
# print (ntice)

# pokus=1,2,3
# print(pokus)

# n1=tuple("Ahoj")
# print (n1)


# n = (10,2)
# n = n + (17,)
# print(n)

"""
Úkol:
1) Vytvořte n-tici s třemi náhodnými čísly a 
   vypište ji.   
2) Vygenerujte cyklem seznam s 10-ti tříprvkovými 
   n-ticemi. Náhodná čísla budou z intervalu <0,1>.
   Seznam celý vypište.
   Nakonec seznam vypište ještě tak, aby n-tice byly pod 
   sebou.
"""

#1
# import random
# # uživatel zadá počet n-tic
# n = int(input("Zadejte počet n-tic: "))
# # vytvoříme n-tice a vypíšeme je
# for i in range(n):
#     ntice = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
#     print(ntice)


#2
import random
seznam=[]
# vytvoříme n-tice a vypíšeme je
for i in range(10):
    ntice = (random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
    print(ntice)
    seznam.append(ntice)

