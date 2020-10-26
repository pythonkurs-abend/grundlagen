def change_string(wort):
    wort = 'abend'


wort = 'morgen'
change_string(wort)
print(wort)


def change_list(l):
    l[1] = 'GEÄNDERT'


liste = ['Bernd', 'Maria', 'Tanja']

change_list(liste)

print(liste)

"""
Referenzen (Pointer) oder Kopien (* / &)

- Primitive Datentypen (int, float, bool, str..)
  -> werden kopiert
- Komplexe Datentypen (list, tuple, dict, object)
  -> werden referenziert

"""

z1 = [3, 4, 5]
z2 = z1
z2[1] = 42

print(z1)
print(id(z1))
print(id(z2))

i1 = 10
i2 = i1
i2 = 42
print(i1)

