"""Napiš proceduru, která vykreslí domeček dané velikosti. Velikost se zadá jako argument, např:

vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)
Proceduru v programu několikrát zavolej (s různými velikostmi)."""


from math import sqrt
from turtle import forward, left, right, exitonclick
from math import sqrt

def vykresli_domecek(velikost):
   
    forward(velikost)
    left(135)
    forward(sqrt(velikost*velikost+velikost*velikost))
    right(135)
    forward(velikost)
    left(-135)
    forward(sqrt(velikost*velikost+velikost*velikost))
    right(135)
    forward(velikost)
    right(45)
    forward(sqrt(velikost*velikost+velikost*velikost)/2)
    right(90)
    forward(sqrt(velikost*velikost+velikost*velikost)/2)
    right(45)
    forward(velikost)
    left(90)
    forward(50)          
   
       
vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)

exitonclick()

