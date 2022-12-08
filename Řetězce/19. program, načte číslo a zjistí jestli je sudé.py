"""Napiš program, který načte číslo a zjistí, jestli je sudé.
Sudá čísla jsou beze zbytku dělitelná dvěma."""


cislo = int(input("Zadej číslo:"))
if cislo % 2 == 0:
    print("Ano")
else:
    print("Ne")