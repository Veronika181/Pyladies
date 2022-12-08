#Napiš program, který bude simulovat hod dvěmi kostkami a vypíše hody na obou kostkách a celkové body.

#Příklad výstupu programu:
##První kostka: 2
#Druhá kostka: 4
#Celkový součet: 6


from random import randrange
kostka1 = randrange (1,7)
kostka2 = randrange (1,7)
print ("První kostka:" , kostka1)
print ("Druhá kostka:" ,kostka2)
print("Součet je:" , kostka1 + kostka2)