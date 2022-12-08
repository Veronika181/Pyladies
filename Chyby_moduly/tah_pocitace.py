"""Napiš funkci tah_pocitace(pole, symbol), která dostane řetězec s herním polem a symbol, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

Použij jednoduchou náhodnou „strategii”:

Vyber číslo od 0 do 19.
Pokud je dané políčko volné, hrej na něj.
Pokud ne, opakuj od bodu 1.
Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_pocitace(pole, symbol):
    Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.

    ...
Zavolání print(tah_pocitace('o-------------------', 'x')) by mohlo vypsat třeba o---------x---------."""

import random


def tah_pocitace(pole, symbol):
    while True:
        nahodna_pozice = random.randrange(0, len(pole))
        if pole[nahodna_pozice] == "-":
            return tah(pole, nahodna_pozice, symbol)


def tah(pole, pozice, symbol):
    if pozice >= len(pole) or pozice < 0:
        print("Tam nejde hrát!")
        return
    elif "x" == pole[pozice] or "o" == pole[pozice]:
        print("Tam nejde hrát!")
        return
    elif symbol != "x" and symbol != "o":
        print("Zvolen špatný symbol")
        return
    else:
        novytah = pole[:pozice] + symbol + pole[pozice + 1:]
        return novytah

print(tah_pocitace("xxxxxxxxxxxxxxxxxxx-", "o"))