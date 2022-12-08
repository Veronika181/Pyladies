#Konec hry
#Když někdo vyhraje nebo dojde k remíze, cyklus se ukončí a vypíše se výsledek – třeba s gratulací nebo povzbuzující zpráva.
#Stav hry kontroluj po každém tahu.Nezapomeň, že máš k dispozici funkci vyhodnot!

import random


def tah_pocitace(pole, symbol):
    while True:
        tah_pocitace = random.randrange(0, len(pole) - 1)
        if pole[tah_pocitace] == "-":
            novytah = pole[:tah_pocitace] + symbol + pole[tah_pocitace + 1:]
            return novytah
        else:
            continue


def tah(pole, pozice, symbol):
    if pozice >= len(pole) or pozice < 0:
        print("Tam nejde hrát!")
        raise ValueError
    if "x" == pole[pozice] or "o" == pole[pozice]:
        print("Tam nejde hrát!")
        raise ValueError
    if symbol != "x" and symbol != "o":
        print("Zvolen špatný symbol")
        raise ValueError
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
        try:
            return tah(pole, cislopozice, symbol)
        except ValueError:
            continue


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def vyhodnoceni_tahu(hernipole):
    if vyhodnot(hernipole) == "!":
        print("Remíza. :-( ")
        return True
    elif vyhodnot(hernipole) == "x":
        print("Vyhrál hráč X. Gratuluji !!!")
        return True
    elif vyhodnot(hernipole) == "o":
        print("Vyhrál hráč O. Gratuluji !!!")
        return True


def piskvorky1d():
    hernipole = '--------------------'
    while True:
        hernipole = tah_hrace(hernipole, "x")
        print(hernipole)
        if vyhodnoceni_tahu(hernipole):
            return
        hernipole = tah_pocitace(hernipole, "o")
        print(hernipole)
        if vyhodnoceni_tahu(hernipole):
            return


piskvorky1d()
