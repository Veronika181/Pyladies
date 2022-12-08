#Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec - buď '+', '-', '*' nebo '/'. Program provede na číslech příslušnou operaci.
#Příklad použití programu:
#První číslo: 123     Druhé číslo: 456     Operace: +   123 + 456 = 579

cislo1 = input("Napiš první číslo:")
cislo2 = input("Napiš druhe číslo:")
Součet_čisel = int(cislo1) + int(cislo2)
print (str(cislo1) + " + " + str(cislo2) + " = " + str(Součet_čisel))