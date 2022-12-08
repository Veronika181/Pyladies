#Zkus přepsat Kámen, Nůžky, Papír pomocí and a or.Dokážeš docílit toho, aby se každý z řetězců 'Remíza.', 'Počítač vyhrál.' a 'Vyhrála jsi!' objevil v programu jen jednou, aniž bys tyhle řetězce musela přiřazovat do proměnných?

from random import randrange
cislo = randrange(3)
tah_hrace = input("Kámen, nůžky, papír, teď: ")

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
