"""Změň program Kámen, Nůžky, Papír tak, aby opakoval hru, dokud uživatel nezadá slovo konec."""

from random import randrange

while True:
        tah_hrace = input("Kámen, nůžky, papír, teď: ")
        if tah_hrace == "konec":
            break

        if tah_hrace != "kámen" and tah_hrace != "nůžky" and tah_hrace != "papír":
            continue

        cislo = randrange(3)        
        if cislo == 0:
            tah_pocitace = "kámen"
        elif cislo == 1:
            tah_pocitace = "nůžky"
        else:
            tah_pocitace = "papír"

        print("Tah počítače je:" , tah_pocitace)
        print("Tah hráče je:" , tah_hrace)
        print()

        if tah_hrace == tah_pocitace:
            print("Remíza")
        elif tah_hrace == "kámen" and tah_pocitace == "papír" or tah_hrace == "papír" and tah_pocitace == "nůžky":
            print("Prohrál jsi")
        elif tah_hrace == "kámen" and tah_pocitace == "nůžky" or tah_hrace == "papír" and tah_pocitace == "kámen":
            print("Vyhrál jsi") 
        else:
            print("Promin znám jen tři slova: kámen, nůžky a papír.")

print("Konec hry")