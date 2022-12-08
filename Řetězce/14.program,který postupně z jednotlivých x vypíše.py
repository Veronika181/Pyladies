"""Napiš program, který postupně z jednotlivých 'X' vypíše:
X
X X
X X X
X X X X"""


for řádek in range(5):
    for sloupec in range(řádek):
        print("X", end ="")
    print()


