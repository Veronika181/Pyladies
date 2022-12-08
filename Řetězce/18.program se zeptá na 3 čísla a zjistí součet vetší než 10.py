"""Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10."""

soucet = 0
for x in range(3):
    cislo = int(input("Zadej "+ str(x+1) +".číslo: "))     
    soucet = soucet + cislo

if soucet >= 10:
    print("Součet čísel je větší než 10")
else:
    print("Součet čísel je menší než 10")
