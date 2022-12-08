"""Napiš program, který se zeptá na příjmení uživatelky/uživatele a zkusí podle něj uhodnout její/jeho pohlaví. To pak vypíše.
(Pohlaví není podle jména možné určit přesně – stačí zvládnout ta nejčastější česká příjmení.)"""


prijmeni = input('Zadej příjmení ')
pohlaví = "ová"

if  pohlaví in prijmeni[-3:]:
    print("Je to pravdepodobně žena.")



