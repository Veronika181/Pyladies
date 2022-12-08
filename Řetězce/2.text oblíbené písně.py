"""Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce a zjisti, kolikrát je v něm použito písmeno K. (Velké nebo malé.)
Text by mělo jít jednoduše vyměnit za jiný.""""



pisnicka = "Maybe it's the way you say my name Maybe it's the way you play your game But it's so good, I've never known anybody like you But it's so good, I've never dreamed of nobody like you And I've hear of a love that comes once in a lifetime And I'm pretty sure that you are that love of mine Cause I'm in a field of Dandelions Wishing on every one that you'll be mine, mine And I see forever in your eyes I feel okay when I see you smile, smile Wishing on dandelions all of time Praying to God that one day you'll be mine Wishing on dandelions all of the time, all of the time"
pocet_k = 0
for c in pisnicka:
        if c == 'k' or c == 'K':
                pocet_k = pocet_k +1
print("Počet 'k' a 'K' v textu je ",pocet_k)







