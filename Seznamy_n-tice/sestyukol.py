"""Napiš funkci vytvor_balicek, která vrátí nový zamíchaný seznam hracích karet pro hru Prší. Každá položka seznamu bude (na rozdíl od balíčku ze setkání) dvojice hodnota-barva.

Hodnoty karet jsou 2-10, 'J', 'Q', 'K', 'A'. Barvy jsou '♥' '♦' '♠' '♣'. (Symboly si můžeš zkopírovat jako text. Nezobrazují-li se ti v příkazové řádce správně, použij místo nich S, K, P, +.)

Například:
from moje_reseni import vytvor_balicek
vytvor_balicek()
[(2, '♥'), (10, '♠'), ('A', '♣'), ..."""


def vytvor_balicek():
    barvy = ['♥', '♦', '♠', '♣']
    hodnoty = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    balicek = []
    for cisla in hodnoty:
        for barva in barvy:
            balicek.append((cisla, barva))
    return balicek


print(vytvor_balicek())
