"""Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah(pole, pozice, symbol):
    Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.

Například:

tah('--------------------', 0, 'x') vrátí 'x-------------------'
tah('--------------------', 19, 'o') vrátí '-------------------o'
tah('x-o-x-o-x-o-x-o-x-o-', 5, 'x') vrátí 'x-o-xxo-x-o-x-o-x-o-'"""

def tah(pole, pozice, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:pozice] + symbol + pole[pozice + 1:]