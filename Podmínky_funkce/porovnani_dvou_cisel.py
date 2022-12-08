#Napiš program, který se zeptá uživatele na dvě čísla a jako výsledek tato dvě čísla porovná.

#Příklad použití programu: První číslo: 10, Druhé číslo: 5, Číslo 10 je větší než číslo 5
prvni_cislo = int(input ("Jaké je první číslo? "))

druhe_cislo = int(input("Jaké je druhé číslo? "))
if (prvni_cislo < druhe_cislo):
    print("Číslo " +str(druhe_cislo)+ " je větší než číslo "+str(prvni_cislo))

elif (prvni_cislo > druhe_cislo):
    print("Číslo " +str(prvni_cislo)+ " je větší než číslo "+str(druhe_cislo))

elif(prvni_cislo==druhe_cislo):
    print("Čísla se rovnají")