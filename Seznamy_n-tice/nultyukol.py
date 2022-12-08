"""Stáhni si soubor s testy, test_piskvorky.py a dej ho do adresáře kde budeš tvořit Piškvorky.

Na ulehčení testování si s aktivním virtuálním prostředím nainstaluj modul pytest-level. Ten umožňuje pouštět jen určité testy – podle toho, jak jsi daleko:

(venv)$ python -m pip install pytest-level
Zkus spustit všechny testy. Asi ti neprojdou:

(venv)$ python -m pytest -v
Pak zkus spustit testy pro úroveň 0:

(venv)$ python -m pytest -v --level 0
Teď se nepustí žádné testy – všechny se přeskočí. Výpis by měl končit nějak takto:

collected N items / N deselected
=== N deselected in 0.01 seconds ===
Zadáš-li v posledním příkazu --level 1, aktivuje se první z testů. Pravděpodobně neprojde – v dalším úkolu ho spravíš!
Tvůj postup vždycky bude:

Když nějaký test neprochází, sprav ho.
Když všechno zezelená, postup na další level/úkol."""



def vytvor_seznam_zvirat():
    return ["pes", "kočka", "králík", "had"]

zvirata = vytvor_seznam_zvirat()
print(zvirata.pop())

print(vytvor_seznam_zvirat())

zvirata
print(zvirata)