#Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.


for i in range(5):

    tip = int(input("Řekni mi číslo: "))

      if i == 0:

        zatim_nejmensi = tip

    if tip < zatim_nejmensi:

        zatim_nejmensi = tip

print("Nejmenší číslo je:", zatim_nejmensi)