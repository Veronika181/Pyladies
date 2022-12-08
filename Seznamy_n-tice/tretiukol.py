"""Napiš funkci obsahuje, která dostane seznam a slovo a zjistí, jestli je to slovo v daném seznamu. Podle toho vrátí True nebo False.
Například:

from moje_reseni import vytvor_seznam_zvirat, obsahuje
zvirata = vytvor_seznam_zvirat()
obsahuje(zvirata, 'pes')
True
obsahuje(zvirata, 'vodováha')
False"""



def vytvor_seznam_zvirat():
    return ["pes", "kočka", "králík", "had"]

seznam = vytvor_seznam_zvirat()

def obsahuje(seznam,slovo):
        if slovo in seznam:
            return True
        else:
            return False

print(obsahuje(seznam,"pes"))
print(obsahuje(seznam, 'vodováha'))
