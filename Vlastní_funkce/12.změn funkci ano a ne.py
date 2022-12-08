"""Změň funkci ano_nebo_ne (kterou jsme si ukazovali v lekci "Definice funkcí") tak, aby se místo ano se dalo použít i a, místo ne i n a aby se nebral ohled na velikost písmen a mezery před/za odpovědí.
Odpovědím jako možná nebo no tak určitě by počítač dál neměl rozumět."""


def ano_nebo_ne(otazka):
     """Vrátí True nebo False podle odpovědi uživatele"""
     while True:
        odpoved = input(otazka).lower().replace(" ","")
        if odpoved == 'ano' or odpoved == 'a':
            return True
        elif odpoved == 'ne' or odpoved == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')