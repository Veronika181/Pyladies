"""Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X"""


for řádek in range(6):
    for sloupec in range(6):
        if řádek == 0 or sloupec == 0 or řádek == 5 or sloupec == 5 :
           print("x", end = "")
        else: print(" ", end = "")
    print("")