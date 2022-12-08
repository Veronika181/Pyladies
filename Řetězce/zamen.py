slovo = input('Slovo: ')
pozice = int(input('Které písmeno zaměnit (od nuly)? '))
novy_znak = input('Nové písmeno: ')

zacatekslova = slovo[:pozice]
konecslova = slovo[pozice + 1:]
nove_slovo = zacatekslova + novy_znak + konecslova

print(nove_slovo)