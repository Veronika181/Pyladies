from tkui import input, nacti_cislo, ano_nebo_ne, print

def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka).lower().replace(" ", "")
        if odpoved == 'ano' or odpoved == 'a':
            return True
        elif odpoved == 'ne' or odpoved == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

