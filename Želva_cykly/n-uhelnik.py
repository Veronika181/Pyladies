from turtle import *

x = int(input("Zadej n-úhelník, který chceš nakreslit."))

for i in range(x):
    forward(200/x)
    left(360/x)
