"""Napiš program, který se zeptá na dva řetězce a zjistí, jestli je jeden obsažen ve druhém. Nebere přitom ohled na velikost písmen."""

a_retezec = input("Napiš první řetězec:")
b_retezec = input("Napiš druhý řetězec:")

if b_retezec.lower() in a_retezec.lower():
    print("První řetězec je obsažen ve druhém řetězci.")
else: 
    print("První řetezec není obažen ve druhém řetezci.")





