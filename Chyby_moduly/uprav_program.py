"""Uprav program z Lekce "Podmínky a funkce", který postupně načte od uživatele dvě čísla a operaci ('+', '-', '*' nebo '/') a provede na číslech příslušnou operaci.

Program uprav tak, aby:

při špatném vstupu napověděl co očekává a zeptal se znovu a
při dělení nulou vypsal hlášku Nulou nelze dělit.
Použij na to ošetření příslušné chyby (tj. ne if delitel == 0:).

Příklad použití:

První číslo: třistatřiatřicet
Zadávej jen čísla
První číslo: 333
Druhé číslo: 0
Operace: /
Nulou nelze dělit."""


def program(prvni_cislo, druhe_cislo):
    operace = input("Jakou operaci program  provede?")
    if operace == "+":
        print("Výsledek u sčítání bude:", prvni_cislo + druhe_cislo)
    elif operace == "-":
        print("Výsledek u odečítání bude:", prvni_cislo - druhe_cislo)
    elif operace == "*":
        print("Výsledek u násobení bude:", prvni_cislo * druhe_cislo)
    elif operace == "/":
        try:
            print("Výsledek u dělení bude:", prvni_cislo / druhe_cislo)
        except ZeroDivisionError:
            print("Nulou nelze dělit!!!")


def zadej_cislo(hlaska):
    while True:
        cislo = input(hlaska)
        try:
            return int(cislo)

        except:
            print("Zadávej jen čísla, zkus to znovu!")


program(zadej_cislo("Jaké je první číslo?"), zadej_cislo("Jaké je druhé číslo?"))
