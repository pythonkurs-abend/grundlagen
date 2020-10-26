def change_zahl(zahl):
    print('Z2', zahl)
    # Lokale Variable
    zahl = 23
    print(id(zahl))
    print('Z5', zahl)


# Globale Variable
zahl = 42

change_zahl(zahl)

print('Z12', zahl)
print(id(zahl))


def change_zahl2():
    # Lokale Variable
    # zahl = 25
    # Holt die globale Variable zahl in den lokalen Namensraum
    global zahl
    zahl = 25
    print('Z20', zahl)


change_zahl2()
print(zahl)
