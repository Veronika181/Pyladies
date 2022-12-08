"""Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že nepoužiješ např. print('X X X X X').

Jak pojmenuješ proměnnou cyklu? A tu druhou?"""


for řádek in range(5):
    for sloupec in range(5):
        print("X",end="")
    print("")