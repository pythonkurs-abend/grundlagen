# Array -> Python -> Liste
name1 = 'Bernd'
name2 = 'Tanja'
name3 = 'Maria'

#           0        1        2
namen = ['Bernd', 'Tanja', 'Maria']

print(type(namen))

print(namen[1])

#         0   1   2   3   4
zahlen = [23, 24, 21, 25, 23]
print(zahlen[0])

# SO NICHT
# namen += 'Neuer Name'

# Sind zwei Listen miteinander verknüpfen
namen += ['Neuer Name']
print(namen)

# .push
namen.append('Noch ein neuer')
print(namen)

# Überprüfung ob ein Objekt in der Liste enthalten ist
print('Tanja' in namen)

# Letzte Element entfernen und zurückgeben
print(namen.pop())
print(namen)

# Letzte Element ausgeben
print(namen[-1])

# Leere Listen sind False
print(not [])

if namen:
    print('noch namen enthalten')

namen[1] = 'ERSETZT'
print(namen)

# Elemente 1 und 2 aus 3 (nicht inklusiv)
print(namen[1:3])
print(namen[0::2])

# [STARTWERT:WIEVIELE:INTERVAL]

# Wie viele Elemente hat unsere Liste überhaupt?
print(len(namen))

# Element löschen
namen.remove('Bernd')

print(namen)

# Strings lassen sich wie Listen behandeln
text = 'Python macht Spaß'
print(text[0:6])

# Mehere Datentypen in einer Liste zu mischen kann zu Problemen führen
schlecht = [42, 'irgendwas', False]

# Mehrdimensionale Listen
# Gleichförmiges Mehrdimensionalles Array
kunden = [['bernd', 'huber'], ['maria', 'förderer']]
print(kunden[1][1])

komplex = [2, [2, 3, [4, [5, [6, [7, 42]]]]]]

print(komplex[1][2][1][1][1][1])
