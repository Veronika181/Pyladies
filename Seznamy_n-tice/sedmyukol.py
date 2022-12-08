"""Úkol na procvičení a vzpomenutí. Už jsi ho jednou vyřešil/a.
Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že každý print vypíše jen jedno X. Nepoužívej tedy např. print('X X X X X') ani print('X ' * 5)."""


for řádek in range(5):
    for sloupec in range(5):
        print("X",end="")
    print("")