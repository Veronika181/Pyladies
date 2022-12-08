"""V modulu piskvorky (tj. v souboru piskvorky.py) napiš funkci tah_hrace(pole, symbol), která dostane řetězec s herním polem a symbol (x nebo o) a:

dostane řetězec s herním polem,
zeptá se hráče, na kterou pozici chce hrát,
pomocí funkce tah zjistí, jak vypadá herní pole se zaznamenaným tahem hráče
vrátí toto herní pole se zaznamenaným tahem hráče.
Pokud uživatel zadá špatný vstup (nečíslo, záporné číslo, obsazené políčko apod.), funkce mu vynadá a zeptá se znova.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    ...
Například zavolání print(tah_hrace('o-------------------', 'x')) by mohlo dopadnout takto:

Kam chceš hrát? nevím
Zadávej čísla!
Kam chceš hrát? 0
Tam nejde hrát!
Kam chceš hrát? -1
Tam nejde hrát!
Kam chceš hrát? 151
Tam nejde hrát!
Kam chceš hrát? 2
o-x-----------------
Nezapomeň, že ve vedlejším modulu máš funkci tah, kterou si můžeš naimportovat.

Funguje-li tahle funkce s příkladem výše, otestuj ji opět pomocí automatických testů. Tentokrát nastav level na 30 až 34. (Testuje se funkce, která volá input. Jak takový test napsat je nad rámec tohoto kurzu.)

Odevzdej celý soubor piskvorky.py (i s funkcí vyhodnot)."""




from util import tah
def vyhodnot(pole):
    if "xxx" in pole:
        return  "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah_hrace(pole, symbol):
    while True:
        pozice = input("Na které pozici chceš hrát?")
        try:
            cislopozice = int(pozice)
        except ValueError:
            print("Zadávej jen čísla!!!")
            continue
        return tah(pole, cislopozice, symbol)