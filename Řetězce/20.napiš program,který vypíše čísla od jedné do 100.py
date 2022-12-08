"""Napiš program, který vypíše čísla od jedné do 100, ale:

Pokud je číslo dělitelné třemi, napíše místo něj „bum”.
Pokud je číslo dělitelné pěti, napíše místo něj „bác”.
Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho „bum-bác”."""

for cislo in range(1,101):
    if cislo % 5 == 0 and cislo % 3 == 0:
        print("bum-bác")
    elif cislo % 3 == 0:
        print("bum")
    elif cislo % 5 == 0:
        print("bác")
    else: 
        print(cislo)
