"""Přepiš funkci tah, aby skončila s chybou ValueError v těchto případech:

Hra na pozici, která není v poli, např. tah('--------------------', -1, 'x')
Hra na obsazené políčko, např. tah('x-------------------', 0, 'o')
Hra jiným symbolem než 'x' nebo 'o', např. tah('--------------------', 0, 'řeřicha')"""

def tah(pole, pozice, symbol):
    if pozice >= len(pole) or pozice < 0:
        raise ValueError("Nejsi v hracím poli")
    if "x" == pole[pozice] or "o" == pole[pozice]:
        raise ValueError("Obsazené políčko")
    if symbol != "x" and symbol != "o":
        raise ValueError("Zvolen špatný symbol")
    else:
        novytah = pole[:pozice] + symbol + pole[pozice + 1:]
        return novytah