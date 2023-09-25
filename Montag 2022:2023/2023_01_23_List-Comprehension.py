# -1 Erstelle eine Liste listeMinus1, die alle Zahlen von 0 bis 49 enthält
# TODO
listeMinus1 =[i for i in range(50)]
# 0. Erstelle eine Liste liste0, die alle Zahlen von 49 bis 0 enthält
# TODO
liste0 = [i for i in range(49, -1, -1)]

# 1. Erstelle eine Liste liste1, die alle geraden Zahlen von 0 bis 400 enthält
# TODO
liste1 = [i for i in range(0, 401, 2)]

# 2. Erstelle eine Liste liste2 aller Quadratzahlen von 0 bis 225 (0 1 4 9 ... 196 225)
# TODO
liste2 = [i*i for i in range(16) ]

# 3. Erstelle eine Liste liste3 aller Zweierpotenzen von 1 bis 1024 (1 2 4 8 ... 512 1024)
# TODO
liste3 = [i**2 for i in range(10)]

# 4. Erstelle eine Liste liste4 der Zahlen 225 196 169 144 121 100 81 64 49 36 25 16 9 4 1 0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225
# TODO
liste4 = [i*i for i in range(15, -16, -1)]
# 5. Erstelle eine Liste liste5 der Zahlen 225 224 221 216 209 200 189 176 161 144 125 104 81 56 29 0
# TODO
liste5 = [225-i*i for i in range(16)]
# 6. Erstelle eine Liste liste6, die 100 Zufallszahlen zwischen -250 und 250 enthält
# TODO
import random
liste6 = [random.randint(-250, 250) for i in range(0, 100)]
# 7. Erstelle eine Liste liste7, die alle positiven Zahlen aus liste6 enthält
# TODO
liste7 = [i for i in liste6 if i > 0]
# 8. Erstelle eine Liste liste8, die alle Quadrate der Zahlen aus liste6 enthält
# TODO
liste8 = [i*i for i in liste6]
# 9. Erstelle eine Liste liste9, die 1000 mal die 0 enthält
# TODO
liste9 = [0 for i in range(1000)]
# 10. Erstelle eine Liste liste10, die 5 mal eine Liste aller Zahlen von 1 bis 5 enthält
# TODO
liste10 = 
# 11. Erstelle eine Liste liste11, die alle Listen [], [1], [1, 2], [1, 2, 3], ..., [1, 2, ..., 99, 100] enthält
# TODO

def listensumme(liste: list) -> int:
    summe = 0
    for zahl in liste:
        summe += zahl
    return summe

# 12. Erstelle eine Liste liste12, die die Summen über alle Listen aus liste11 enthält
# Verwende die Funktion listensumme
# TODO

# 13. Erstelle eine Liste liste13, die alle Zahlen aus liste12 enthält, die durch 3 teilbar sind
# TODO

# 14. Erstelle eine Liste liste14, die 10 Listen mit jeweils 10 zufälligen Zahlen zwischen 1 und 10 enthält
# TODO

# 15. Erstelle eine Liste liste15, die 10 Listen mit jeweils einer zufälligen, zwischen 1 und 10 großen, Anzahl an zufälligen
# Elementen zwischen 1 und 10 enthält
# TODO

# 16. Erstelle eine Liste liste16, die eine zufällige, zwischen 1 und 10 große, Anzahl an Listen mit
# TODO

# 17. Erstelle eine Liste liste17, die alle Primzahlen zwischen 2 und 1000 enthält
# TODO
#mit %(rest)

