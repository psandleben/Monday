# 1. Eine Funktion, die rekursiv die Fakultät von n berechnet und zurückgibt
'''
def fakultät(n: int) -> int:
    if n == 0:
        return 1
    return n * fakultät(n - 1)

print(fakultät(24))
'''
def fakultät_kompakt(n: int) -> int:
    return 1 if n == 0 else n * fakultät(n - 1)
    
'''
# 2. Eine Funktion, die rekursiv die Quersumme von n berechnet und zurückgibt
def quersumme(n: int) -> int:
    if n < 10:
        return n
    letzte_zahl = n % 10
    n_ohne_letzte_zahl = n // 10
    return quersumme(n_ohne_letzte_zahl) + letzte_zahl

def quersumme_kompakt(n: int) -> int:
    return n if n < 10 else quersumme_kompakt(n // 10) + n % 10


# 3. Eine Funktion, die rekursiv bestimmt, ob s ein Palindrom ist,
# Falls ja, gibt sie True zurück, ansonsten False
def palindrom(s: str) -> bool:
    if len(s) <= 1:
        return True
    erster_buchstabe = s[0]
    letzter_buchstabe = s[-1]
    if erster_buchstabe != letzter_buchstabe:
        return False
    s_ohne_ersten_und_letzten_buchstaben = s[1:-1]
    return palindrom(s_ohne_ersten_und_letzten_buchstaben)

def palindrom(s: str) -> bool:
    return len(s) <= 1 or (s[0] == s[-1] and palindrom(s[1:-1]))


# 4. Eine Funktion, die rekursiv die n'te Fibonacci-Zahl berechnet und zurückgibt.
# Die 0'te Fibonacci-Zahl ist 0, die 1'te 1, usw.
def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_kompakt(n: int) -> int:
    return n if n <= 1 else fibonacci_kompakt(n - 1) + fibonacci_kompakt(n - 2)



# 5. Eine Funktion, die für eine Zahl n die möglichen Kompositionen folgender Funktionen
# bestimmt und ausgibt, um mit ihnen auf den Wert 1 zu kommen:
# 1. (n + 1) / 4
# 2. (n + 3) / 4
# 3. (3 * n + 1) / 4
# Für 9 wäre es beispielsweise 2 -> 1, denn:
# (9 + 3) / 4 = 3
# (3 + 1) / 4 = 1

def kompositionen_h(n: int, bisherige_komposition: str) -> None:
    pass

def kompositionen(n: int) -> None:
    kompositionen_h(n, "")


# 6. Schreibe eine Funktion zwei_hoch, die einen einzigen Integer-Parameter n besitzt.
# Die Funktion soll rekursiv die n'te Potenz von 2 berechnen und zurückgeben.
def zwei_hoch(n: int) -> int:
    if n == 0:
        return 1
    zwei_hoch_vorgänger = zwei_hoch(n - 1)
    zwei_hoch_n = zwei_hoch_vorgänger * 2
    return zwei_hoch_n

def zwei_hoch_kompakt(n: int) -> int:
    return 1 if n == 0 else 2 * zwei_hoch_kompakt(n - 1)


# 7. Schreibe eine Funktion m_hoch, die zwei Integer-Parameter m und n besitzt.
# Die Funktion soll rekursiv die n'te Potenz von m berechnen und zurückgeben.
def m_hoch(m: int, n: int) -> int:
    if n == 0:
        return 1
    zahl_vorgänger = m_hoch(n - 1)
    m_hoch_n = zahl_vorgänger * m
    return m_hoch_n

# 8. Schreibe eine Funktion listensumme, die einen einzigen Listen-Parameter l besitzt.
# Die Funktion soll rekursiv die Summe aller Zahlen in l berechnen und zurückgeben.
def listensumme(l: list) -> int:
    return 0 if len(l) == 0 else l[0] + listensumme(l[1:])

# 9. Schreibe eine Funktion fakultätenliste, die einen einzigen Integer-Parameter n besitzt.
# Die Funktion soll rekursiv eine Liste der ersten n Fakultäten erstellen und zurückgeben.
def fakultätenliste(n: int) -> list:
    if n == 1:
        return [1]
    fakultätenliste_vorgänger = fakultätenliste(n - 1)
    return [1] if n == 1 else fakultätenliste_vorgänger + [fakultätenliste_vorgänger[-1] * n]

# 5 ergibt [1, 2, 6, 24, 120]
# listensumme([1, 2, 3, 4]) = 1 + listensumme([2, 3, 4]) = 1 + (2 + listensumme([3, 4])) = 1 + (2 + (3 + listensumme([4]))) = 1 + (2 + (3 + (4 + listensum([]))))
# = 1 + (2 + (3 + (4 + 0))) = 1 + (2 + (3 + 4)) = 1 + (2 + 7) = 1 + 9 = 10

# 2 ** 4
# -> 2 ** 3 
# -> 2 ** 2
# -> 2 ** 1

# 2 ** n

# 2 ** 9: 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
# 2 ** 10: 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
# 2 ** 11: 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2

# 2048 / 2 = 

# 10! = 10 * 9!

# Schreibe eine Funktion potenzenliste, die einen einzigen Integer-Parameter n besitzt.
# Die Funktion soll rekursiv eine Liste der ersten n Zweierpotenzen erstellen und zurückgeben.
def potenzenliste(n: int) -> list:
    if n == 1:
        return [1]
    potenzenliste_vorgänger = potenzenliste(n - 1)
    potenzenliste_n = potenzenliste_vorgänger + [2 ** (n - 1)] # Variante 1
    potenzenliste_n = potenzenliste_vorgänger + [potenzenliste_vorgänger[-1] * 2] # Variane 2
    return potenzenliste_n

# Schreibe eine Funktion ggT, die zwei Integer-Parameter m und n besitzt.
# Die Funktion soll rekursiv den größten gemeinsamen Teiler von m und n bestimmen und zurückgeben.
# TODO
'''