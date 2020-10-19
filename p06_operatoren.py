# Vergleichsoperatoren

print(42 == 42)

# Python überprüft Inhalt UND Datentyp
print(42 == '42')
print(42 == int('42'))

print('Ungleich', 42 != 42)

# > < >= <= !=
zahl = 42

# if zahl > 10 and zahl < 50:
#    print('TRUE')
if 10 < zahl < 50:
    print('TRUE')

# Logischen Operatoren
# und, oder, nicht
# && || !

"""
true  and true = true
true  and false = false
false and true = false
false and false = false
"""

if 42 == 42 and 42 > 200:
    print('Ist wahr')

"""
true  and true = true
true  and false = true
false and true = true
false and false = false
"""
if 42 == 42 or 42 > 200:
    print('Oder ist wahr')

print(not True)
print(not False)

# False: 0 '' None [] () {}
# True: Alles andere

if 42:
    print('42 ist wahr')

if 0:
    print('0 ist wahr')

if 'welt':
    print('welt ist wahr')

if '':
    print('leerer string ist?')

wort = None

if wort:
    print('Wort ist leer')

if ' ':
    print('Leerzeichen?')

if ['Anne']:
    print('Anne ist wahr')

if []:
    print('Leere Liste ist wahr')

xyz = None

if xyz == None:
    # Schlechter Stil
    pass

if xyz is None:
    # Guter Stil
    pass

if xyz is not None:
    pass

wahr = True

if wahr is True:
    pass
