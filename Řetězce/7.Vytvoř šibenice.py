"""Vytvoř hru Šibenice podle následujícího popisu.

Počítač náhodně zvolí slovo (zatím třeba ze tří možností). Pro jednoduchost používej malá písmena a nepoužívej slova, ve kterých se stejné písmeno opakuje dvakrát (třeba čokoláda).

Zkus třeba slova: trávník, stromek, stavení.
Výchozí stav je řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
Výchozí počet neúspěšných pokusů je nula.
Stále dokola:

Zeptej se hráče na písmeno.
Pokud je to písmeno ve vybraném slově:
Zaměň ve stavu příslušné podtržítko za ono písmeno. (Bude se hodit řetězcová metoda index a podprogram zamen* ze srazu.)
Pokud dané písmeno není ve vybraném slově:
započítej neúspěšný pokus.
Vypiš stav (slovo s případnými podtržítky).
Pokud už ve stavu nejsou podtržítka:
Pogratuluj hráči.
Ukonči hru.
Vypiš počet neúspěšných pokusů.
Pokud je počet neúspěšných pokusů 9 (nebo víc):
Dej hráči najevo, že prohrál.
Ukonči hru."""


from random import randrange

cislo = randrange(3)
if(cislo == 0):
    slovo = "trávník"

if(cislo == 1):
    slovo = "stavení"

if(cislo == 2):
    slovo = "stromek"

slovo = "stromek"
stav = "_______"
neuspesnepokusy = 0 

while (True): 
    písmeno = input("Řekni mi písmeno: ")
    if písmeno in slovo:
        index = slovo.index(písmeno)
        stav = stav[:index] + písmeno + stav[index + 1:]
    else:
        neuspesnepokusy = neuspesnepokusy + 1
    print(stav)
    if "_" not in stav:
        print("Gratuluji k výhře.")
        break
    print("Počet neúspěšných pokusů je:", neuspesnepokusy)
    if neuspesnepokusy >= 9:
        print("Prohrál jsi.")
        break
    





 