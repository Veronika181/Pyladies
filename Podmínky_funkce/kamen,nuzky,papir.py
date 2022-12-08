#Do proměnné tah_pocitace dá náhodně slovo 'kámen', 'nůžky' nebo 'papír'. (Koukni na předchozí úkol!)
#Zeptá se uživatele na tah; výsledek uloží do proměnné tah_hrace
#Je-li tah hráče 'kámen':
#je-li tah počítače 'kámen':
#vypíše 'Remíza!';
#jinak, je-li tah počítače 'nůžky':
#vypíše 'Vyhrál jsi!';
#jinak, je-li tah počítače 'papír':
#vypíše 'Prohrál jsi!'.
#Jinak, je-li tah hráče 'nůžky':
#je-li tah počítače 'kámen':
#vypíše 'Prohrál jsi!';
#jinak, je-li tah počítače 'nůžky':
#vypíše 'Remíza!';
#jinak, je-li tah počítače 'papír':
#vypíše 'Vyhrál jsi!'.
#Jinak, je-li tah hráče 'papír':
#je-li tah počítače 'kámen':
#vypíše 'Vyhrál jsi!';
#jinak, je-li tah počítače 'nůžky':
#vypíše 'Prohrál jsi!';
#jinak, je-li tah počítače 'papír':
##vypíše 'Remíza!'.
###Jinak,
####Omluví se (vypíše hlášku), že zná jen tři slova: kámen, nůžky a papír.

from random import randrange

cislo = randrange(3)

tah_hrace = input("Kámen, nůžky, papír, teď: ")

if cislo == 0:
    tah_pocitace = "kámen"
elif cislo == 1:
    tah_pocitace = "nůžky"
else:
    tah_pocitace = "papír"

print("Tah počítače je: " + tah_pocitace + " a tvůj tah je : " + tah_hrace)

if tah_hrace == 'kámen':
    if tah_pocitace == "kámen":
        print('Remíza!')
    elif tah_pocitace == 'nůžky':
        print("Vyhrál jsi!")
    elif tah_pocitace == 'papír':
        print("Prohrál jsi!")
elif tah_hrace == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Prohrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Remíza!')
    elif tah_pocitace == 'papír':
        print('Vyhrál jsi!')
elif tah_hrace == ('papír'):
    if tah_pocitace == 'kámen':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Prohrál jsi!')
    elif tah_pocitace == 'papír':
        print('Remíza!')
else:
    print("Promin znám jen tři slova: kámen, nůžky a papír.")