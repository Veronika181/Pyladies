"""Předchozí 4 programy s cyklem for uprav tak, aby počet řádků (či velikost čtverce/trojúhelníku/tabulky) mohl zadat uživatel."""


i = int(input("Zadej hodnotu:"))

for řádek in range(i):
    for sloupec in range(i):
        print(řádek * sloupec, end=" ")
    print()
print("")

for řádek in range(i):
    for sloupec in range(1,řádek +1):
        print("X", end ="")
    print("",end="\n")
print("")

for x in range(i):  
    if x == 0:  
        print("první řádek")        
    else:
        print("není první")
print("")

for řádek in range(i):
    for sloupec in range(i):
        if řádek == 0 or sloupec == 0 or řádek == i-1 or sloupec == i-1 :
           print("x", end = "")
        else: print(" ", end = "")
    print("")