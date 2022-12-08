def vytvor_seznam_zvirat():
    return ["pes", "kočka", "králík", "had"]

seznam = vytvor_seznam_zvirat()

pismeno_k = []


for slovo in seznam:
    if slovo[0] == 'k':
        pismeno_k.append(slovo)


print(pismeno_k)