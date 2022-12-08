"""Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

"x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
"o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
"!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
Například:

vyhodnot('--------------------') vrátí '-'
vyhodnot('--o--xxx---o--o-----') vrátí 'x'
vyhodnot('xoxoxoxoxoxoxoxoxoxo') vrátí '!'"""

# krizky "xxx"
#kolečka "ooo"
#vykricniky "!!!"
#pomlcky "---"

pole = "-"


def vyhodnot(pole):
    if "xxx" in pole:
        return  "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"