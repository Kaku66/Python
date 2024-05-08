# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:09:24 2011

@author: Radek
"""

import math
uhel=0
mista=2
print("uhel\tsin\tcos\ttan\tcotg")
while uhel<=90:
    radiany=math.radians(uhel)
    sinus=round(math.sin(radiany),mista)
    cosinus=round(math.cos(radiany),mista)
    if uhel!=90:
        tangens=round(math.tan(radiany),mista)
    else:
        tangens="Inf."
    if uhel!=0:  
        cotg=round(1/math.tan(radiany),mista)
    else:
        cotg="Inf."        

    print(str(uhel)+"°","\t",sinus,"\t",cosinus,"\t",tangens,"\t",cotg)
    uhel=uhel+5
    
    
    
    
  




  
    
    
    
    
    
    
    
