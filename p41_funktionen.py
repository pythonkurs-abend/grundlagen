def get_sinn():
    return 42


print(get_sinn())


def addiere(zahl1, zahl2, zahl3=0):
    return zahl1 + zahl2 + zahl3


ergebnis = addiere(3, 4, 5)
print(ergebnis)


"""Ermittelt den Sinn

Description:
Lange Beschreibung

Returns:
    bool
"""
def is_sinn(zahl:int):
    if zahl == 42:
        return True

    return False


def is_sinn_besser(zahl):
    return zahl == 42


is_sinn(42)

