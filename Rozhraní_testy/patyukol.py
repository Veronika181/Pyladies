from ctvrtyukol import tah, tah_pocitace


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
