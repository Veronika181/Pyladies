#V modulu piskvorky (tj. v souboru piskvorky.py) napiš funkci piskvorky1d, která:

#Vytvoří řetězec s herním polem
#Stále dokola:
#zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
#vypíše stav hry
#zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
#vypíše stav hry
#Zatím nemusíš řešite konec hry (pokud ho už nemáš z minula).

#V modulu hra (tj. v souboru hra.py) přidej import a volání funkce piskvorky1d.

#Původní testy by měly stále procházet. Automatické testy na celou hru ale nejsou – otestuj to ručně pomocí python hra.py!

#Tady odevzdej pouze modul piskvorky.py.



from util import tah
from ai import tah_pocitace


def tah_hrace(pole, symbol):
    while True:
        pozice = input("Na které pozici chceš hrát?")
        try:
            cislopozice = int(pozice)
        except ValueError:
            print("Zadávej jen čísla!!!")
            continue
        return tah(pole, cislopozice, symbol)


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