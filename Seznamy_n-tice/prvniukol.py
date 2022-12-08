"""Napiš funkci filtruj_kratka_jmena, která dostane seznam řetězců a vrátí seznam těch, které jsou kratší než 5 písmen.
Například:
>>> from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
>>> zvirata = vytvor_seznam_zvirat()
>>> filtruj_kratka_jmena(zvirata)
['pes', 'had']
Vzpomeň si, jak se vytváří seznam: začni s prázdným seznamem a postupně přidávej prvek po prvku.

Funkce by měla opět vracet nový seznam a svůj argument nechat nezměněný. Vyzkoušej si to následujícím „dialogem“:

from moje_reseni import vytvor_seznam_zvirat, filtruj_kratka_jmena
zvirata = vytvor_seznam_zvirat()
filtruj_kratka_jmena(zvirata)
['pes', 'had']
 zvirata
['pes', 'kočka', 'králík', 'had']"""




def vytvor_seznam_zvirat():
    return ["pes", "kočka", "králík", "had"]

seznam = vytvor_seznam_zvirat()

def filtruj_kratka_jmena(seznam):
    k_Seznam = []
    for slovo in seznam:
        if len(slovo) < 5:
            k_Seznam.append(slovo)
    return k_Seznam


print(filtruj_kratka_jmena(seznam()))

