"""Napiš funkci piskvorky1d, která:

Vytvoří řetězec s herním polem, '--------------------'
Stále dokola:
zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
vypíše herní pole
zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
vypíše herní pole
Zatím neřeš konec hry."""

import random
def tah_pocitace(pole, symbol):
    while(True):
        tah_pocitace = random.randrange(0,len(pole)-1)
        if pole[tah_pocitace] == ("-"):
            novytah = pole[:tah_pocitace] + symbol + pole[tah_pocitace + 1:]
            return novytah
        else:
            continue
def tah(pole, pozice, symbol):
    if pozice >= len(pole) or pozice < 0:
        print("Tam nejde hrát!")
        return tah_hrace(pole,symbol)
    elif "x" == pole[pozice] or "o" == pole[pozice]:
        print("Tam nejde hrát!")
        return tah_hrace(pole,symbol)
    elif symbol != "x" and symbol != "o":
        print("Zvolen špatný symbol")
        return tah_hrace(pole,symbol)
    else:
        novytah = pole[:pozice] + symbol + pole[pozice + 1:]
        return novytah
def tah_hrace(pole, symbol):
    while True:
        pozice = input("Na které pozici chceš hrát?")
        try:
            cislopozice = int(pozice)
        except ValueError:
            print("Zadávej jen čísla!!!")
            continue
        return tah(pole,cislopozice,symbol)

def piskvorky1d():
        hernipole = '--------------------'
        while(True):
                hernipole = tah_hrace(hernipole,"x")
                print(hernipole)
                hernipole = tah_pocitace(hernipole,"o")
                print(hernipole)

piskvorky1d()