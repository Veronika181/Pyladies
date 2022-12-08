"""Úkol na procvičení a vzpomenutí. Už jsi ho jednou vyřešil/a.

Napiš program, který vypíše „tabulku“ s násobilkou.

0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
0 3 6 9 12
0 4 8 12 16"""


for řádek in range(5):
    for sloupec in range(5):
        print(řádek * sloupec, end=" ")
    print()