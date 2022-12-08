#Napiš program na hádání čísel od 1 do 9. Program si bude "myslet" nějaké číslo od 1 do 9 včetně a uživatel bude toto číslo hádat. Při uhádnutí se vypíše počet pokusů, které uživatel potřeboval pro uhádnutí čísla.

#Příklad použití programu:

#####Myslím na číslo od 1 do 9.
####Zkus hádat, jaké číslo to je!
###Zadej číslo zde: 1
##Zadej číslo zde: 5
#Zadej číslo zde: 8
#Gratuluji! Myslel jsem na číslo 8. Uhádl/a jsi na 3. pokus.

from random import randrange
generovanecislo = randrange(1,10)
tip = 0
pokus = 0
print("Myslím na číslo od 1 do 9. Zkus hádat, jaké je číslo to je!")
while(tip != generovanecislo):
    pokus = pokus + 1
    tip = int(input("Zadej číslo:"))
print("Gratuluji, Myslel jsem číslo", tip, ". Uhádl/a jsi na", pokus, ".pokus")