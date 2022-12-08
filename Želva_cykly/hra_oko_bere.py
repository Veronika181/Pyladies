########Naprogramuj hru Oko bere:

#######Začínáš se skóre 0 bodů.
######V každém kole:
#####Počítač vypíše, kolik máš bodů.
####Počítač se zeptá, jestli chceš pokračovat.
###Pokud byla odpověď „ne“:
##Hra končí.
#Jinak:
##Počítač „vybere kartu“ – náhodně vybere číslo od 2 do 10;
#vybranou hodnotu vypíše;
#křičte tuto hodnotu ke skóre.
#Pokud máš víc než 21 bodů:
####Počítač vypíše, že prohráváš;
###hra končí.
##Po skončení hry počítač vypíše dosažené skóre.
#Cílem hry je neprohrát a získat přitom co nejvíc bodů, ideálně 21.

from random import randrange

skóre = 0
while skóre < 21:
    print("Tvůj součet bodů je", skóre)
    odpověd = input("Chceš pokračovat ve hře? ")
    if odpověd == "ano":
        karta = randrange(2, 11)
        print("Vybraná karta: ", karta)
        skóre = skóre + karta
    elif odpověd == "ne":
        break
    else:
        print("""Nerozumím", Potřebuji odpověd "ano", nebo "ne""")

if skóre == 21:
    print("Gratuluji, Jsi vítěz!")
elif skóre > 21:
    print("Škoda!", skóre, "tvoje skore je příliš vysoké!")
else:
    print("Chybí ti jen", 21 - skóre, "bodů")
