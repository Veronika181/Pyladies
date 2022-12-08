"""V modulu ai (tj. v souboru ai.py) napiš funkci tah_pocitace(pole, symbol), která dostane řetězec s herním polem a symbol, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

Nejde-li na dané pole hrát, funkce musí skončit s chybou ValueError.

Použij jednoduchou náhodnou „strategii”:

Vyber číslo od 0 do 19.
Pokud je dané políčko volné, hrej na něj.
Pokud ne, opakuj od bodu 1.
Navíc k tomu funkce nesmí „zamrznout“ (způsobit nekonečný cyklus), ať jí předáš jakékoli hodnoty argumentů. Kdyby strategie výše měla „zamrznout“, funkce ať místo toho způsobí ValueError.
Hlavička funkce by tedy měla vypadat nějak takhle:
def tah_pocitace(pole, symbol):
Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.

Zavolání print(tah_pocitace('o-------------------', 'x')) by mohlo vypsat třeba o---------x---------.
Testy jsou v levelech 40 až 44.
Odevzdej celý soubor ai.py"""


import random
from util import tah

def tah_pocitace(pole, symbol):
    while True:
        nahodna_pozice = random.randrange(0, len(pole))
        if pole[nahodna_pozice] == "-":
            return tah(pole, nahodna_pozice, symbol)
        if "-" not in pole:
            raise ValueError