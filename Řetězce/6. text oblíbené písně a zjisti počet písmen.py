"""Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce a zjisti, kolik je v něm písmen. Nepočítej mezery, znaky nového řádku a znaky !"#$%&\'()*+,-./:;<=>?@[\]^_{|}~.
Text písně by mělo jít jednoduše vyměnit za jiný.

Postup:
Na začátku nastav počet nalezených písmen na 0.
Pro každý znak textu:
Když znak není obsažen v ! " # $ % & …:
Zvyš počet nalezených písmen o 1.
Vypiš počet nalezených písmen.
Bonus: Zkusíš najít v dokumentaci řetězcovou metodu, která ti pomůže spočítat jen alfanumerické znaky? Získáš stejný výsledek?"""


pisnicka = "Maybe it's the way you say my name Maybe it's the way you play your game But it's so good, I've never known anybody like you But it's so good, I've never dreamed of nobody like you And I've hear of a love that comes once in a lifetime And I'm pretty sure that you are that love of mine Cause I'm in a field of Dandelions Wishing on every one that you'll be mine, mine And I see forever in your eyes I feel okay when I see you smile, smile Wishing on dandelions all of time Praying to God that one day you'll be mine Wishing on dandelions all of the time, all of the time"
pocet_nalezenych_pismen = 0
nepocitane_znaky= '!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'

for kazdyznaktextu in pisnicka:
    if kazdyznaktextu.isalpha():      
        pocet_nalezenych_pismen = pocet_nalezenych_pismen + 1
        
print("Počet nalezených písmen : ", pocet_nalezenych_pismen)

