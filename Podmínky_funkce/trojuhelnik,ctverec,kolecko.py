from random import randrange
cislo= randrange(3)

if cislo == 0:
    tvar = "trojúhelník"
elif cislo == 1:
    tvar = "čtverec"
else:
    tvar = "kolečko"
print(tvar)