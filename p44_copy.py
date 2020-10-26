from copy import copy, deepcopy

z1 = [2, 3, 4]

# Das erstellt eine Kopie der Zahlen
z2 = copy(z1)

z2[1] = 42
print(z1)

i1 = [1, [2, 3]]
i2 = copy(i1)

i2[0] = 42
print(i1)

# Das ist noch i1
i2[1][0] = 66
print(i1)

# Alle Ebenen kopieren
i3 = deepcopy(i1)
i3[1][1] = 88
print(i1)

kunden = [
    {'vorname': 'Bernd', 'nachname': 'Huber', 'addressen': [
        {'strasse': 'Musterweg 42'},
        {'strasse': 'Musterweg 43'},
    ]},
    {'vorname': 'Tanja', 'nachname': 'Förderer'},
]
