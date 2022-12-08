"""Napiš program, který simuluje tuto „hru“:
První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.)
Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.
Nápověda: průběžně stačí ukládat jen údaj o tom, kdo vede a kolik má bodů.
Tip: Program si napiš napřed v češtině; pak ho přelož do Pythonu."""

from random import randrange
vitez = 0
pocetboduviteze = 0
hod = 0

for cislohrace in range(1,5):
    pocet_bodu = 0
    while hod != 6:
        hod = randrange(1, 6+1)
        pocet_bodu = pocet_bodu + 1
        print (f'Hráč {cislohrace} hodil {hod}')
    print(f'Hráč {cislohrace} má {pocet_bodu} bodů.')
    hod = 0
    if pocet_bodu > pocetboduviteze:
        vitez = cislohrace
        pocetboduviteze = pocet_bodu

print(f'Vyhrál hráč {vitez}, který má {pocetboduviteze} bodů.')

